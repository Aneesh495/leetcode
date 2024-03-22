/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const result = [];
    for (let start = 0; start < arr.length; start += size) {
        result.push(arr.slice(start, start + size));
    }
    return result;
};