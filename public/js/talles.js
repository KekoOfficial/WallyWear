// Public size helper methods
const Talles = {
    fetchSizesForCategory: async function(category) {
        try {
            const data = await Utils.api.fetch(`/api/talles/categoria/${category}`);
            return data || [];
        } catch (e) {
            console.error("Error fetching sizes:", e);
            return [];
        }
    }
};
