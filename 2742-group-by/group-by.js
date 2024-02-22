/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const groups = {};
    for (const item of this) {
        const key = fn(item);
        if (!Object.prototype.hasOwnProperty.call(groups, key)) {
            groups[key] = [];
        }
        groups[key].push(item);
    }
    return groups;
};