document.addEventListener("DOMContentLoaded", () => {
    const footer = document.createElement("footer");
    footer.style.cssText = "background: #1a1a1a; color: white; padding: 3rem 1rem; margin-top: 4rem; text-align: center;";

    const redes = Utils.storage.get("redes_sociales") || [
        { nombre: "WhatsApp", url: "https://wa.me/595981000000", activo: true },
        { nombre: "Instagram", url: "https://instagram.com/mallywear", activo: true }
    ];

    let redesHTML = "";
    redes.filter(r => r.activo).forEach(r => {
        redesHTML += `<a href="${r.url}" target="_blank" style="color: white; margin: 0 15px; text-decoration: none; font-weight: 500;">${r.nombre}</a>`;
    });

    footer.innerHTML = `
        <div style="max-width: 1000px; margin: 0 auto;">
            <h2 style="margin-bottom: 1rem;">Mally Wear</h2>
            <p style="color: #ccc; margin-bottom: 2rem;">Calidad y estilo en cada prenda.</p>
            <div style="margin-bottom: 2rem;">
                ${redesHTML}
            </div>
            <hr style="border: 0; border-top: 1px solid #333; margin-bottom: 2rem;">
            <p style="font-size: 0.8rem; color: #888;">&copy; ${new Date().getFullYear()} Mally Wear - Paraguay. Todos los derechos reservados.</p>
        </div>
    `;

    document.body.appendChild(footer);
});
