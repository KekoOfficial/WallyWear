let productosList = [];
let productoSeleccionado = null;
let tallesLocales = [];

window.addEventListener("DOMContentLoaded", async () => {
    await cargarProductos();
});

async function cargarProductos() {
    try {
        productosList = await Utils.api.fetch("/api/productos/");
        const select = document.getElementById("select-producto");
        select.innerHTML = '<option value="">-- Selecciona un producto --</option>';

        // Filter by category if window.categoryFilter is set
        const filtered = productosList.filter(p => {
            if (!window.categoryFilter) return true;
            return p.categoria.toLowerCase() === window.categoryFilter.toLowerCase();
        });

        filtered.forEach(p => {
            const opt = document.createElement("option");
            opt.value = p.id;
            opt.textContent = `${p.nombre} (${p.categoria})`;
            select.appendChild(opt);
        });
    } catch (err) {
        alert("Error al cargar productos: " + err.message);
    }
}

async function seleccionarProducto() {
    const id = document.getElementById("select-producto").value;
    const editor = document.getElementById("talles-editor");

    if (!id) {
        editor.style.display = "none";
        productoSeleccionado = null;
        tallesLocales = [];
        return;
    }

    productoSeleccionado = productosList.find(p => p.id == id);
    if (productoSeleccionado) {
        document.getElementById("producto-titulo").textContent = `Talles de: ${productoSeleccionado.nombre}`;

        // Fetch current sizes
        try {
            // Check if talles is string or array
            let currentTalles = productoSeleccionado.talles || [];
            if (typeof currentTalles === 'string') {
                currentTalles = JSON.parse(currentTalles);
            }
            tallesLocales = currentTalles;
        } catch (e) {
            tallesLocales = [];
        }

        renderTallesGrid();
        editor.style.display = "block";
    }
}

function renderTallesGrid() {
    const grid = document.getElementById("grid-calzado") || document.getElementById("grid-talles");
    grid.innerHTML = "";

    const available = window.availableSizes || [];
    available.forEach(size => {
        const div = document.createElement("div");
        div.className = `size-box ${tallesLocales.includes(size) ? 'selected' : ''}`;
        div.textContent = size;
        div.onclick = () => toggleSize(size, div);
        grid.appendChild(div);
    });
}

function toggleSize(size, element) {
    if (tallesLocales.includes(size)) {
        tallesLocales = tallesLocales.filter(s => s !== size);
        element.classList.remove("selected");
    } else {
        tallesLocales.push(size);
        element.classList.add("selected");
    }
}

async function guardarTalles() {
    if (!productoSeleccionado) return;

    try {
        const result = await Utils.api.fetch(`/api/talles/producto/${productoSeleccionado.id}`, {
            method: 'POST',
            body: JSON.stringify({ talles: tallesLocales })
        });
        if (result.success) {
            alert("✅ Talles guardados con éxito");
            // Refresh list
            await cargarProductos();
            document.getElementById("select-producto").value = productoSeleccionado.id;
            await seleccionarProducto();
        }
    } catch (err) {
        alert("Error al guardar talles: " + err.message);
    }
}
