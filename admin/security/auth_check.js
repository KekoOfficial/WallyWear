(function() {
    const auth = sessionStorage.getItem('admin_auth');
    const currentPath = window.location.pathname;

    // Si no está autenticado y no está en la página de login, redirigir
    if (auth !== 'true') {
        if (!currentPath.includes('/login/')) {
            // Determinar la ruta relativa al login dependiendo de dónde estemos
            // Si estamos en /admin/index.html -> login/index.html
            // Si estamos en /admin/products/index.html -> ../login/index.html

            // Una forma segura es usar una ruta relativa al directorio admin
            // Buscamos cuántos niveles subir hasta llegar a la carpeta admin
            const pathParts = currentPath.split('/');
            const adminIndex = pathParts.indexOf('admin');

            if (adminIndex !== -1) {
                const levels = pathParts.length - adminIndex - 2;
                let redirectPath = '';
                for(let i=0; i<levels; i++) redirectPath += '../';
                redirectPath += 'login/index.html';
                window.location.href = redirectPath;
            } else {
                // Fallback si por alguna razón no detecta 'admin' en la ruta
                window.location.href = '/admin/login/index.html';
            }
        }
    }
})();
