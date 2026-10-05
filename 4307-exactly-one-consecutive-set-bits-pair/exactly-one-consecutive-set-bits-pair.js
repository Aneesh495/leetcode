/**
 * @param {number} n
 * @return {boolean}
 */
var consecutiveSetBits = function(n) {
    // A bit survives only when its immediate higher neighbor is also set.
    const adjacent = n & (n >>> 1);
    return adjacent !== 0 && (adjacent & (adjacent - 1)) === 0;
};