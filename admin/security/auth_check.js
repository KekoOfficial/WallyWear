/**
 * Wally Wear - Control de Acceso Admin
 */

(function() {
    const auth = sessionStorage.getItem("admin_auth");
    const currentPath = window.location.pathname;

    // Si no está autenticado y no está en la página de login, redirigir
    if (auth !== "true" && !currentPath.includes("admin/login/")) {
        window.location.href = "../login/index.html";
    }
})();

function cerrarSesion() {
    sessionStorage.removeItem("admin_auth");
    window.location.href = "../login/index.html";
}
