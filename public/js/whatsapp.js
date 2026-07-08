// Public WhatsApp link generation helper
const WhatsApp = {
    getWhatsAppConfig: async function() {
        try {
            return await Utils.api.fetch("/api/whatsapp/config");
        } catch (e) {
            console.error("Error getting WhatsApp config:", e);
            return { numero: "" };
        }
    },

    openChat: function(number, text) {
        const cleanNumber = number.replace("INACTIVE:", "").replace("+", "");
        const url = `https://api.whatsapp.com/send?phone=${cleanNumber}&text=${encodeURIComponent(text)}`;
        window.open(url, "_blank");
    }
};
