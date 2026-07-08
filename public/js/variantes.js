// Public variants helper methods
const Variantes = {
    fetchVariantsForProduct: async function(productId) {
        try {
            const data = await Utils.api.fetch(`/api/variantes/producto/${productId}`);
            return data || [];
        } catch (e) {
            console.error("Error fetching variants:", e);
            return [];
        }
    }
};
