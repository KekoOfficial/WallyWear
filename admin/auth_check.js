function checkAuth() {
    const auth = sessionStorage.getItem("admin_auth");
    if (auth !== "true") {
        window.location.href = "0_acceso_admin.html";
    }
}
checkAuth();
