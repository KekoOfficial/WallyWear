document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const pedidoId = urlParams.get('id');

    if (!pedidoId) {
        document.getElementById("detalle-container").innerHTML = "<p>ID de pedido no especificado.</p>";
        return;
    }

    cargarDetallePedido(pedidoId);
});

async function cargarDetallePedido(id) {
    const container = document.getElementById("detalle-container");
    try {
        const p = await Utils.api.fetch(`/api/detalle_pedido/${id}`);
        if (!p) {
            container.innerHTML = "<p>Pedido no encontrado.</p>";
            return;
        }

        // Mocking address, payment method and items list view
        const direccion = p.direccion || "Retiro en sucursal";
        const metodoPago = p.metodo_pago || "Transferencia Bancaria";
        const totalFormateado = Utils.formatCurrency(p.total);

        let comprobanteHTML = "";
        if (p.comprobante) {
            comprobanteHTML = `
                <div class="detail-row" style="flex-direction: column; align-items: flex-start;">
                    <span class="label">Comprobante de Pago:</span>
                    <img class="comprobante-img" src="../../uploads/comprobantes/${p.comprobante}" alt="Comprobante" onerror="this.src='https://via.placeholder.com/300x400?text=Comprobante+no+disponible'">
                </div>
            `;
        } else {
            comprobanteHTML = `
                <div class="detail-row">
                    <span class="label">Comprobante de Pago:</span>
                    <span class="value" style="color: #dc3545; font-weight: bold;">No adjuntado</span>
                </div>
            `;
        }

        container.innerHTML = `
            <div class="card">
                <div class="detail-row">
                    <span class="label">ID de Pedido:</span>
                    <span class="value" style="font-weight: bold;">${p.id}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Fecha y Hora:</span>
                    <span class="value">${p.fecha}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Nombre del Cliente:</span>
                    <span class="value">${p.cliente_nombre || 'No especificado'}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Teléfono del Cliente:</span>
                    <span class="value">${p.cliente_telefono || 'No especificado'}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Dirección de Entrega:</span>
                    <span class="value">${direccion}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Método de Pago:</span>
                    <span class="value">${metodoPago}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Talle del Pedido:</span>
                    <span class="value">${p.talla || 'Especificado por ítem'}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Variante del Pedido:</span>
                    <span class="value">${p.variante || 'Especificado por ítem'}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Total a Pagar:</span>
                    <span class="value" style="font-size: 1.2rem; font-weight: bold; color: #007bff;">${totalFormateado}</span>
                </div>
                <div class="detail-row">
                    <span class="label">Estado del Pedido:</span>
                    <span class="value" style="font-weight: bold; text-transform: uppercase;">${p.estado}</span>
                </div>
                ${comprobanteHTML}

                <a href="productos_pedido.html?id=${p.id}" class="btn btn-items">📦 Ver Prendas del Pedido</a>

                <div class="actions">
                    <button onclick="confirmarPedido('${p.id}')" class="btn btn-confirm" ${p.estado === 'pagado' ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>Confirmar Pago (Suma stock)</button>
                    <button onclick="cancelarPedido('${p.id}')" class="btn btn-cancel" ${p.estado === 'cancelado' ? 'disabled style="opacity:0.5; cursor:not-allowed;"' : ''}>Cancelar Pedido</button>
                </div>
            </div>
        `;
    } catch (err) {
        container.innerHTML = "<p>Error al cargar el detalle del pedido.</p>";
    }
}

async function confirmarPedido(id) {
    if (!confirm("¿Deseas confirmar el pago de este pedido y descontar el stock correspondiente?")) return;
    try {
        const response = await Utils.api.fetch(`/api/pedidos/${id}/confirmar`, { method: 'POST' });
        alert("✅ " + response.message);
        cargarDetallePedido(id);
    } catch (err) {
        alert("Error: " + err.message);
    }
}

async function cancelarPedido(id) {
    if (!confirm("¿Deseas cancelar este pedido?")) return;
    try {
        const response = await Utils.api.fetch(`/api/pedidos/${id}/cancelar`, { method: 'POST' });
        alert("✅ " + response.message);
        cargarDetallePedido(id);
    } catch (err) {
        alert("Error: " + err.message);
    }
}
