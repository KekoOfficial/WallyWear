/**
 * Wally Wear - Gestión de Pedidos
 */

document.addEventListener("DOMContentLoaded", function() {
    cargarPedidos();
});

function cargarPedidos() {
    const contenedor = document.getElementById("lista-pedidos");
    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    if (!contenedor) return;

    contenedor.innerHTML = "";

    // Ordenar de más reciente a más antiguo
    pedidos.sort((a, b) => {
        const timeA = a.id.startsWith("PED-") ? parseInt(a.id.split('-')[1]) : 0;
        const timeB = b.id.startsWith("PED-") ? parseInt(b.id.split('-')[1]) : 0;
        return timeB - timeA;
    });

    if (pedidos.length === 0) {
        contenedor.innerHTML = "<p>No hay pedidos registrados</p>";
        return;
    }

    pedidos.forEach((pedido) => {
        let detalle = pedido.productos.map(p => `${p.nombre} x${p.cantidad} = Gs ${(p.precio * p.cantidad).toLocaleString()}`).join("<br>");

        const div = document.createElement("div");
        div.className = "pedido";
        div.innerHTML = `
            <h3>ID: ${pedido.id}</h3>
            <p>Fecha: ${pedido.fecha}</p>
            <p>Estado: <strong>${pedido.estado}</strong></p>
            <p>Productos:<br>${detalle}</p>
            <p>Total: Gs ${pedido.total.toLocaleString()}</p>
            ${pedido.estado === "Pendiente de pago" ?
                `<button onclick="confirmarPago('${pedido.id}')">✅ Confirmar pago recibido</button>` :
                `<span>✅ Pago confirmado</span>`
            }
            <button onclick="eliminarPedido('${pedido.id}')" style="background: #dc3545; margin-left: 10px;">Eliminar</button>
        `;
        contenedor.appendChild(div);
    });
}

function confirmarPago(id) {
    const pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    const index = pedidos.findIndex(p => p.id === id);
    if (index !== -1) {
        pedidos[index].estado = "Pago confirmado - En preparación";
        localStorage.setItem("pedidos", JSON.stringify(pedidos));
        cargarPedidos();
        alert("✅ Pedido confirmado correctamente");
    }
}

function eliminarPedido(id) {
    if (!confirm("¿Estás seguro de eliminar este pedido?")) return;

    let pedidos = JSON.parse(localStorage.getItem("pedidos")) || [];
    pedidos = pedidos.filter(p => p.id !== id);
    localStorage.setItem("pedidos", JSON.stringify(pedidos));
    cargarPedidos();
}
