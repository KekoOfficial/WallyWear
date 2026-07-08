document.addEventListener("DOMContentLoaded", async () => {
    await cargarWhatsAppConfig();

    const activeToggle = document.getElementById("whatsapp-activo");
    if (activeToggle) {
        activeToggle.addEventListener("change", function() {
            const label = document.getElementById("toggle-label");
            label.textContent = this.checked ? "Activo" : "Inactivo";
        });
    }
});

async function cargarWhatsAppConfig() {
    const numInput = document.getElementById("numero-whatsapp");
    const activeToggle = document.getElementById("whatsapp-activo");
    const label = document.getElementById("toggle-label");

    try {
        const config = await Utils.api.fetch("/api/whatsapp/config");
        if (config && config.numero) {
            // Check if it has active prefix or custom flag
            let num = config.numero;
            let active = true;

            if (num.startsWith("INACTIVE:")) {
                num = num.replace("INACTIVE:", "");
                active = false;
            }

            if (numInput) numInput.value = num;
            if (activeToggle) {
                activeToggle.checked = active;
                if (label) label.textContent = active ? "Activo" : "Inactivo";
            }
        }
    } catch (err) {
        console.error("Error al cargar config de WhatsApp:", err);
    }
}

async function guardarWhatsAppConfig() {
    const numInput = document.getElementById("numero-whatsapp");
    const activeToggle = document.getElementById("whatsapp-activo");

    if (!numInput) return;

    let num = numInput.value.trim();
    if (num && !/^\+5959[0-9]{8}$/.test(num)) {
        alert("Formato de número incorrecto. Debe comenzar con +5959 seguido de 8 números (Ej: +595981123456)");
        return;
    }

    const isActive = activeToggle ? activeToggle.checked : true;
    let finalValue = num;
    if (!isActive) {
        finalValue = "INACTIVE:" + num;
    }

    try {
        const response = await Utils.api.fetch("/api/whatsapp/config", {
            method: 'POST',
            body: JSON.stringify({ numero: finalValue })
        });
        if (response.success) {
            alert("✅ Configuración de WhatsApp guardada exitosamente!");
        }
    } catch (err) {
        alert("Error al guardar: " + err.message);
    }
}
