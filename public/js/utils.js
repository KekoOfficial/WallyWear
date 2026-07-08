const Utils = {
    formatCurrency: function(amount) {
        return "Gs " + amount.toLocaleString('es-PY');
    },

    storage: {
        get: function(key) {
            const data = localStorage.getItem(key);
            return data ? JSON.parse(data) : null;
        },
        set: function(key, value) {
            localStorage.setItem(key, JSON.stringify(value));
        },
        remove: function(key) {
            localStorage.removeItem(key);
        }
    },

    updateCartCounter: function() {
        const carrito = this.storage.get("carrito") || [];
        const contador = document.getElementById("contador") || document.getElementById("contador-carrito");
        if (contador) {
            contador.textContent = carrito.reduce((a, b) => a + b.cantidad, 0);
        }
    }
};
