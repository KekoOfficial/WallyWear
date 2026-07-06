function checkAuth() {
    const auth = sessionStorage.getItem("admin_auth");
    if (auth !== "true") {
        window.location.href = "../login/index.html";
    }
}
checkAuth();
