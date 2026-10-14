/**
 * @param {number[]} nums
 * @param {number} a
 * @param {number} b
 * @return {number}
 */
var minAdjacentSwaps = function(nums, a, b) {
    let middle = 0, high = 0, swaps = 0;
    for (const value of nums) {
        // Every inverted pair belongs to two different target partitions.
        if (value < a) swaps += middle + high;
        else if (value <= b) {
            swaps += high;
            middle++;
        } else high++;
    }
    return swaps % 1000000007;
};