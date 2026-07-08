/**
 * Wally Wear - Lógica del Carrito
 */

document.addEventListener("DOMContentLoaded", function() {
    mostrarCarrito();
});

function mostrarCarrito() {
    const contenedor = document.getElementById("lista-carrito");
    const totalContenedor = document.getElementById("total-final");
    const carrito = Utils.obtenerLocal("carrito", []);

    if (!contenedor) return;
    contenedor.innerHTML = "";
    let total = 0;

    if (carrito.length === 0) {
        contenedor.innerHTML = "<p class='mensaje-vacio'>Tu carrito está vacío</p>";
        if (totalContenedor) totalContenedor.innerHTML = "";
        document.getElementById("btn-pedir").style.display = "none";
        return;
    }

    document.getElementById("btn-pedir").style.display = "block";

    carrito.forEach((item, index) => {
        const subtotal = item.precio * item.cantidad;
        total += subtotal;

        const itemDiv = document.createElement("div");
        itemDiv.className = "item-carrito";
        itemDiv.innerHTML = `
            <div class="item-info">
                <h4>${item.nombre}</h4>
                <p>Precio: ${Utils.formatearGs(item.precio)}</p>
                <div class="cantidad-controles">
                    <button onclick="cambiarCantidad(${index}, -1)">-</button>
                    <span>${item.cantidad}</span>
                    <button onclick="cambiarCantidad(${index}, 1)">+</button>
                </div>
                <p>Subtotal: ${Utils.formatearGs(subtotal)}</p>
            </div>
            <button class="btn-eliminar" onclick="quitarDelCarrito(${index})">Eliminar</button>
        `;
        contenedor.appendChild(itemDiv);
    });

    if (totalContenedor) {
        totalContenedor.innerHTML = `<h3>Total a pagar: ${Utils.formatearGs(total)}</h3>`;
    }
}

function cambiarCantidad(index, delta) {
    let carrito = Utils.obtenerLocal("carrito", []);
    if (carrito[index]) {
        carrito[index].cantidad += delta;
        if (carrito[index].cantidad < 1) {
            carrito.splice(index, 1);
        }
        Utils.guardarLocal("carrito", carrito);
        mostrarCarrito();
        Utils.actualizarContador();
    }
}

function quitarDelCarrito(index) {
    let carrito = Utils.obtenerLocal("carrito", []);
    carrito.splice(index, 1);
    Utils.guardarLocal("carrito", carrito);
    mostrarCarrito();
    Utils.actualizarContador();
}

function generarPedido() {
    const carrito = Utils.obtenerLocal("carrito", []);
    if (carrito.length === 0) return alert("El carrito está vacío");

    const idPedido = "PED-" + Date.now();
    const pedidos = Utils.obtenerLocal("pedidos", []);
    const total = carrito.reduce((a, b) => a + (b.precio * b.cantidad), 0);

    const nuevoPedido = {
        id: idPedido,
        fecha: new Date().toLocaleString(),
        productos: carrito,
        total: total,
        estado: "Pendiente de pago"
    };

    pedidos.push(nuevoPedido);
    Utils.guardarLocal("pedidos", pedidos);
    Utils.guardarLocal("carrito", []);

    mostrarCarrito();
    Utils.actualizarContador();

    const mensajeWhatsApp = `Hola Wally Wear! Mi pedido es: ${idPedido}. Total: ${Utils.formatearGs(total)}.`;

    document.getElementById("resultado-pedido").innerHTML = `
        <div class="aviso">
            <h3>✅ Pedido creado con éxito</h3>
            <p>Tu ID de pedido: <strong>${idPedido}</strong></p>
            <p>Envía este ID por WhatsApp para confirmar tu compra.</p>
            <a href="https://wa.me/595981000000?text=${encodeURIComponent(mensajeWhatsApp)}" target="_blank" class="btn-whatsapp">Enviar a WhatsApp</a>
        </div>
    `;
}
