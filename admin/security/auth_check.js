(function() {
    const auth = sessionStorage.getItem('admin_auth');
    if (auth !== 'true') {
        const currentPath = window.location.pathname;
        // Si estamos en /admin/1_panel_productos.html, necesitamos ir a ./login/index.html (dentro de admin)
        // O si usamos rutas absolutas si es posible, pero en local puede variar.
        // Asumiendo estructura: /admin/1_panel_productos.html y /admin/login/index.html
        // Desde /admin/file.html -> login/index.html es correcto.

        // Verificamos si ya estamos en la página de login para evitar bucle
        if (!currentPath.includes('/login/')) {
            window.location.href = 'login/index.html';
        }
    }
})();
