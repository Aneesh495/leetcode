/**
 * @param {number[]} nums
 * @param {number} minK
 * @param {number} maxK
 * @return {number}
 */
var countSubarrays = function(nums, minK, maxK) {
    let total = 0;
    let run = 0;
    for (const value of nums) {
        run = value >= minK && value <= maxK ? run + 1 : 0;
        // All valid suffixes ending at this element have length at most run.
        total += run;
    }
    return total;
};