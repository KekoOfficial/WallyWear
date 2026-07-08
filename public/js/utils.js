const Utils = {
    formatCurrency: function(amount) {
        return "Gs " + parseInt(amount).toLocaleString('es-PY');
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

    api: {
        async fetch(url, options = {}) {
            try {
                const response = await fetch(url, {
                    ...options,
                    headers: {
                        'Content-Type': 'application/json',
                        ...options.headers
                    }
                });
                if (!response.ok) {
                    const error = await response.json();
                    throw new Error(error.message || error.error || 'Error en la petición');
                }
                return await response.json();
            } catch (err) {
                console.error('API Error:', err);
                throw err;
            }
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
