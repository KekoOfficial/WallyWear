function cargarRedesFooter() {
    const redes = JSON.parse(localStorage.getItem("redes")) || [
        { nombre: "Instagram", url: "#", estado: "Activo" },
        { nombre: "Facebook", url: "#", estado: "Activo" }
    ];

    // Crear footer si no existe
    let footer = document.querySelector("footer");
    if (!footer) {
        footer = document.createElement("footer");
        document.body.appendChild(footer);
    }

    footer.innerHTML = `
        <div id="redes-footer" style="margin-bottom: 1rem;"></div>
        <p>&copy; ${new Date().getFullYear()} Mally Wear - Todos los derechos reservados</p>
    `;
    footer.style.background = "#1a1a1a";
    footer.style.color = "white";
    footer.style.textAlign = "center";
    footer.style.padding = "2rem";
    footer.style.marginTop = "4rem";

    const contenedor = document.getElementById("redes-footer");
    redes.filter(r => r.estado === "Activo").forEach(r => {
        const link = document.createElement("a");
        link.href = r.url;
        link.textContent = r.nombre;
        link.target = "_blank";
        link.style.margin = "0 10px";
        link.style.color = "white";
        link.style.textDecoration = "none";
        link.style.fontWeight = "bold";
        contenedor.appendChild(link);
    });
}
window.addEventListener('DOMContentLoaded', cargarRedesFooter);
