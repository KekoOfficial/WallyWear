// Public orders helper methods
const Pedido = {
    createOrder: async function(payload) {
        try {
            return await Utils.api.fetch("/api/pedidos/", {
                method: "POST",
                body: JSON.stringify(payload)
            });
        } catch (e) {
            console.error("Error creating order:", e);
            throw e;
        }
    },

    uploadReceipt: async function(pedidoId, file) {
        if (!file) return null;
        const formData = new FormData();
        formData.append("comprobante", file);

        try {
            const r = await fetch(`/api/comprobantes/${pedidoId}`, {
                method: "POST",
                body: formData
            });
            return await r.json();
        } catch (e) {
            console.error("Error uploading receipt:", e);
            return null;
        }
    }
};
