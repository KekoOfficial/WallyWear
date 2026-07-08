let productosList = [];
let productoSeleccionado = null;
let variantesLocales = [];

window.onload = async () => {
    await cargarProductos();
};

async function cargarProductos() {
    try {
        productosList = await Utils.api.fetch("/api/productos/");
        const select = document.getElementById("select-producto");
        select.innerHTML = '<option value="">-- Selecciona un producto --</option>';
        productosList.forEach(p => {
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
    const editor = document.getElementById("variantes-editor");

    if (!id) {
        editor.style.display = "none";
        productoSeleccionado = null;
        variantesLocales = [];
        return;
    }

    productoSeleccionado = productosList.find(p => p.id == id);
    if (productoSeleccionado) {
        document.getElementById("producto-titulo").textContent = `Variantes de: ${productoSeleccionado.nombre}`;

        // Fetch current variants
        try {
            variantesLocales = await Utils.api.fetch(`/api/variantes/producto/${productoSeleccionado.id}`) || [];
            // If it is a string representation of an array, parse it, otherwise handle it
            if (typeof variantesLocales === 'string') {
                variantesLocales = JSON.parse(variantesLocales);
            }
        } catch (e) {
            variantesLocales = [];
        }

        renderVariantes();
        editor.style.display = "block";
    }
}

function renderVariantes() {
    const container = document.getElementById("lista-variantes");
    container.innerHTML = "";

    if (variantesLocales.length === 0) {
        container.innerHTML = "<p style='color: #888; margin: 5px;'>Sin variantes cargadas. Agrega una nueva abajo.</p>";
        return;
    }

    variantesLocales.forEach((v, index) => {
        const span = document.createElement("span");
        span.className = "variant-tag";
        span.innerHTML = `
            ${v}
            <button onclick="eliminarVarianteLocal(${index})">&times;</button>
        `;
        container.appendChild(span);
    });
}

function agregarVarianteLocal() {
    const input = document.getElementById("nueva-variante");
    const valor = input.value.trim();

    if (!valor) return;
    if (variantesLocales.includes(valor)) {
        alert("Esta variante ya existe para este producto.");
        return;
    }

    variantesLocales.push(valor);
    input.value = "";
    renderVariantes();
}

function eliminarVarianteLocal(index) {
    variantesLocales.splice(index, 1);
    renderVariantes();
}

async function guardarVariantesServidor() {
    if (!productoSeleccionado) return;

    try {
        const result = await Utils.api.fetch(`/api/variantes/producto/${productoSeleccionado.id}`, {
            method: 'POST',
            body: JSON.stringify({ variantes: variantesLocales })
        });
        if (result.success) {
            alert("✅ Variantes guardadas con éxito");
            // Reload list internally
            await cargarProductos();
            document.getElementById("select-producto").value = productoSeleccionado.id;
            await seleccionarProducto();
        }
    } catch (err) {
        alert("Error al guardar variantes: " + err.message);
    }
}
