var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.filter(Boolean).map(compactObject);
    }
    if (obj !== null && typeof obj === 'object') {
        for (const key of Object.keys(obj)) {
            if (!obj[key]) delete obj[key];
            else obj[key] = compactObject(obj[key]);
        }
    }
    return obj;
};