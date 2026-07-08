(async function() {
    try {
        const response = await fetch('/api/auth/check');
        const data = await response.json();

        const currentPath = window.location.pathname;
        if (!data.authenticated && !currentPath.includes('0_acceso_admin.html')) {
            window.location.href = '0_acceso_admin.html';
        }
    } catch (err) {
        console.error('Auth check error:', err);
    }
})();
