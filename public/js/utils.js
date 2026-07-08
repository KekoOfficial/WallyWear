/**
 * Wally Wear - Utilidades Generales
 */

const Utils = {
    /**
     * Formatea un número como moneda Guaraníes (Gs)
     * @param {number} monto
     * @returns {string}
     */
    formatearGs: function(monto) {
        return "Gs " + Math.round(monto).toLocaleString('es-PY');
    },

    /**
     * Actualiza el contador del carrito en el encabezado
     */
    actualizarContador: function() {
        const carrito = JSON.parse(localStorage.getItem("carrito")) || [];
        const total = carrito.reduce((a, b) => a + b.cantidad, 0);
        const elementos = document.querySelectorAll("#contador, #contador-carrito");
        elementos.forEach(el => el.textContent = total);
    },

    /**
     * Obtiene datos de localStorage con un valor por defecto
     * @param {string} clave
     * @param {any} valorDefecto
     * @returns {any}
     */
    obtenerLocal: function(clave, valorDefecto = []) {
        try {
            return JSON.parse(localStorage.getItem(clave)) || valorDefecto;
        } catch (e) {
            return valorDefecto;
        }
    },

    /**
     * Guarda datos en localStorage
     * @param {string} clave
     * @param {any} valor
     */
    guardarLocal: function(clave, valor) {
        localStorage.setItem(clave, JSON.stringify(valor));
    }
};

// Ejecutar actualización de contador al cargar el script si el DOM ya está listo
if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", Utils.actualizarContador);
} else {
    Utils.actualizarContador();
}
