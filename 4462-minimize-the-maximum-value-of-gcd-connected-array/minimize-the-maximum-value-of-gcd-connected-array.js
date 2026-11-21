/**
 * @param {number} n
 * @param {number} index
 * @param {number} value
 * @return {number}
 */
var minimumMaxValue = function(n, index, value) {
    if (value === 1) return -1;
    let smallestFactor = value;
    for (let p = 2; p * p <= value; p++) {
        if (value % p === 0) { smallestFactor = p; break; }
    }
    // The nearest valid neighbor on each side is even. All other gaps are at least two.
    const maxBefore = (value - smallestFactor) / 2;
    if (index > maxBefore) return -1;
    const after = n - index - 1;
    return after === 0 ? value : value + smallestFactor + 2 * (after - 1);
};