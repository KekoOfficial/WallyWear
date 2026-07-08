/**
 * Wally Wear - Gestión de Productos
 */

document.addEventListener("DOMContentLoaded", function() {
    // La verificación de acceso se manejará en auth_check.js
    cargarCategorias();
    cargarProductosAdmin();
});

function cargarCategorias() {
    const cats = JSON.parse(localStorage.getItem("categorias")) || ["Remeras", "Zapatillas", "Pantalones"];
    const select = document.getElementById("categoria");
    if (!select) return;

    select.innerHTML = "";
    cats.forEach(c => {
        const opt = document.createElement("option");
        opt.value = c;
        opt.textContent = c;
        select.appendChild(opt);
    });
}

function crearCategoria() {
    const nombre = document.getElementById("nueva-cat").value.trim();
    if (!nombre) return alert("Escribe un nombre");

    let cats = JSON.parse(localStorage.getItem("categorias")) || ["Remeras", "Zapatillas", "Pantalones"];
    if (cats.includes(nombre)) return alert("Ya existe");

    cats.push(nombre);
    localStorage.setItem("categorias", JSON.stringify(cats));
    cargarCategorias();
    document.getElementById("nueva-cat").value = "";
    alert("✅ Categoría creada");
}

function guardarProducto() {
    const nombre = document.getElementById("nombre").value.trim();
    const precio = parseInt(document.getElementById("precio").value);
    const stock = parseInt(document.getElementById("stock").value);
    const imagen = document.getElementById("imagen").value.trim();
    const categoria = document.getElementById("categoria").value;

    if (!nombre || isNaN(precio) || isNaN(stock) || !imagen) {
        return alert("Completa todos los campos correctamente");
    }

    const productos = JSON.parse(localStorage.getItem("productos")) || [];
    const nuevo = {
        id: Date.now(),
        nombre, precio, stock, imagen, categoria
    };

    productos.push(nuevo);
    localStorage.setItem("productos", JSON.stringify(productos));

    // Limpiar campos
    document.getElementById("nombre").value = "";
    document.getElementById("precio").value = "";
    document.getElementById("stock").value = "";
    document.getElementById("imagen").value = "";

    cargarProductosAdmin();
    alert("✅ Producto guardado");
}

function cargarProductosAdmin() {
    const contenedor = document.getElementById("lista-admin");
    const productos = JSON.parse(localStorage.getItem("productos")) || [];
    if (!contenedor) return;

    contenedor.innerHTML = "";

    if (productos.length === 0) {
        contenedor.innerHTML = "<p>No hay productos registrados.</p>";
        return;
    }

    productos.forEach(p => {
        const div = document.createElement("div");
        div.className = "prod-admin";
        div.innerHTML = `
            <div class="prod-info">
                <strong>${p.nombre}</strong> | ${p.categoria} <br>
                Precio: Gs ${p.precio.toLocaleString()} | Stock: ${p.stock} <br>
                Imagen: ${p.imagen}
            </div>
            <button onclick="eliminarProducto(${p.id})" style="background: #dc3545;">Eliminar</button>
        `;
        contenedor.appendChild(div);
    });
}

function eliminarProducto(id) {
    if (!confirm("¿Estás seguro de eliminar este producto?")) return;

    let productos = JSON.parse(localStorage.getItem("productos")) || [];
    productos = productos.filter(p => p.id !== id);
    localStorage.setItem("productos", JSON.stringify(productos));
    cargarProductosAdmin();
}
