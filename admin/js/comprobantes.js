// Comprobantes administrative JS helpers
const Comprobantes = {
    getReceiptUrl: function(filename) {
        if (!filename) return null;
        return `/uploads/comprobantes/${filename}`;
    },

    previewReceipt: function(imgElementId, filename) {
        const img = document.getElementById(imgElementId);
        if (img) {
            const url = this.getReceiptUrl(filename);
            if (url) {
                img.src = url;
                img.style.display = 'block';
            } else {
                img.style.display = 'none';
            }
        }
    },

    uploadReceipt: async function(pedidoId, fileInputId) {
        const fileInput = document.getElementById(fileInputId);
        if (!fileInput || !fileInput.files[0]) {
            alert("Selecciona un archivo primero.");
            return null;
        }

        const formData = new FormData();
        formData.append("comprobante", fileInput.files[0]);

        try {
            const response = await fetch(`/api/comprobantes/${pedidoId}`, {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (result.success) {
                return result.filename;
            } else {
                throw new Error(result.message || "Error al subir");
            }
        } catch (err) {
            console.error("Error subiendo comprobante:", err);
            alert("No se pudo subir el comprobante: " + err.message);
            return null;
        }
    }
};
