(function() {
    const auth = sessionStorage.getItem('admin_auth');
    if (!auth) {
        // Redirigir al login si no hay sesión activa
        window.location.href = '/admin/login/index.html';
    }
})();
