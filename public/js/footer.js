(function() {
    function renderFooter() {
        const socialLinks = JSON.parse(localStorage.getItem('social_links')) || {
            whatsapp: 'https://wa.me/595981123456',
            instagram: 'https://instagram.com/wallywear',
            facebook: '',
            tiktok: ''
        };

        const footerHTML = `
            <footer style="background: #1a1a1a; color: white; padding: 2rem; text-align: center; margin-top: 3rem; border-top: 3px solid #333;">
                <div style="margin-bottom: 1rem;">
                    <h3>Wally Wear</h3>
                    <p>Moda Urbana a tu alcance - Paraguay</p>
                </div>
                <div style="margin-bottom: 1rem;">
                    ${socialLinks.whatsapp ? `<a href="${socialLinks.whatsapp}" target="_blank" style="color: #25D366; margin: 0 10px; text-decoration: none; font-size: 1.5rem;"><i class="fab fa-whatsapp"></i> WhatsApp</a>` : ''}
                    ${socialLinks.instagram ? `<a href="${socialLinks.instagram}" target="_blank" style="color: #E1306C; margin: 0 10px; text-decoration: none; font-size: 1.5rem;"><i class="fab fa-instagram"></i> Instagram</a>` : ''}
                    ${socialLinks.facebook ? `<a href="${socialLinks.facebook}" target="_blank" style="color: #4267B2; margin: 0 10px; text-decoration: none; font-size: 1.5rem;"><i class="fab fa-facebook"></i> Facebook</a>` : ''}
                    ${socialLinks.tiktok ? `<a href="${socialLinks.tiktok}" target="_blank" style="color: #00f2ea; margin: 0 10px; text-decoration: none; font-size: 1.5rem;"><i class="fab fa-tiktok"></i> TikTok</a>` : ''}
                </div>
                <p>&copy; 2024 Wally Wear. Todos los derechos reservados.</p>
                <div style="margin-top: 10px;">
                    <a href="/public/3_politica_privacidad.html" style="color: #aaa; text-decoration: none; font-size: 0.9rem;">Políticas y Privacidad</a>
                </div>
            </footer>
        `;

        const existingFooter = document.querySelector('footer');
        if (existingFooter) {
            existingFooter.outerHTML = footerHTML;
        } else {
            document.body.insertAdjacentHTML('beforeend', footerHTML);
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', renderFooter);
    } else {
        renderFooter();
    }
})();
