/**
 * @param {number} n
 * @return {number}
 */
var minimumFlips = function(n) {
    const bits = n.toString(2);
    let flips = 0;
    for (let i = 0; i < bits.length; i++) {
        if (bits[i] !== bits[bits.length - 1 - i]) flips++;
    }
    return flips;
};