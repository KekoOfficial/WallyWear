const Utils = {
    formatCurrency: function(amount) {
        return 'Gs ' + amount.toLocaleString('es-PY');
    },
    getLocalStorage: function(key, defaultValue = []) {
        try {
            const item = localStorage.getItem(key);
            return item ? JSON.parse(item) : defaultValue;
        } catch (e) {
            console.error('Error reading localStorage', e);
            return defaultValue;
        }
    },
    setLocalStorage: function(key, value) {
        try {
            localStorage.setItem(key, JSON.stringify(value));
        } catch (e) {
            console.error('Error writing localStorage', e);
        }
    },
    updateCartCounter: function() {
        const cart = this.getLocalStorage('carrito');
        const counter = document.getElementById('contador') || document.getElementById('contador-carrito');
        if (counter) {
            counter.textContent = cart.reduce((total, item) => total + item.cantidad, 0);
        }
    }
};
