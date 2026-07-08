/**
 * Wally Wear - Lógica de la Tienda (Catálogo)
 */

document.addEventListener("DOMContentLoaded", function() {
    cargarProductos();
});

function cargarProductos() {
    const productos = Utils.obtenerLocal("productos", []);
    const categorias = Utils.obtenerLocal("categorias", ["Remeras", "Zapatillas", "Pantalones"]);
    const contenedor = document.getElementById("contenedor-tienda");

    if (!contenedor) return;
    contenedor.innerHTML = "";

    if (productos.length === 0) {
        contenedor.innerHTML = "<p class='mensaje-vacio'>No hay productos disponibles por el momento.</p>";
    }

    categorias.forEach(cat => {
        const productosCat = productos.filter(p => p.categoria === cat);
        // Ocultar categoría si no tiene productos, a menos que no haya productos en total
        if (productosCat.length === 0 && productos.length > 0) return;

        const section = document.createElement("section");
        section.className = "categoria";
        section.id = `cat-${cat.toLowerCase().replace(/\s+/g, '-')}`;

        section.innerHTML = `
            <h2>${cat}</h2>
            <div class="productos-lista"></div>
        `;

        const lista = section.querySelector(".productos-lista");
        productosCat.forEach(p => {
            const productoCard = document.createElement("div");
            productoCard.className = "producto";
            productoCard.innerHTML = `
                <img src="../images/${p.imagen}" alt="${p.nombre}" onerror="this.src='https://via.placeholder.com/250x220?text=Sin+Imagen'">
                <h3>${p.nombre}</h3>
                <p class="precio">${Utils.formatearGs(p.precio)}</p>
                <p class="stock">Stock disponible: ${p.stock}</p>
                <button onclick="agregarAlCarrito(${p.id})" ${p.stock < 1 ? "disabled" : ""}>
                    ${p.stock < 1 ? "Sin stock" : "Agregar al carrito"}
                </button>
            `;
            lista.appendChild(productoCard);
        });

        if (productosCat.length > 0 || productos.length === 0) {
            contenedor.appendChild(section);
        }
    });
}

function agregarAlCarrito(id) {
    const productos = Utils.obtenerLocal("productos", []);
    const prod = productos.find(x => x.id === id);

    if (!prod || prod.stock < 1) {
        alert("❌ Lo sentimos, no hay stock de este producto.");
        return;
    }

    let carrito = Utils.obtenerLocal("carrito", []);
    const existe = carrito.find(x => x.id === id);

    if (existe) {
        existe.cantidad++;
    } else {
        carrito.push({
            id: prod.id,
            nombre: prod.nombre,
            precio: prod.precio,
            imagen: prod.imagen,
            cantidad: 1
        });
    }

    Utils.guardarLocal("carrito", carrito);
    Utils.actualizarContador();

    // Feedback visual (opcional: mini notificación en vez de alert)
    alert(`✅ ${prod.nombre} agregado al carrito`);
}
