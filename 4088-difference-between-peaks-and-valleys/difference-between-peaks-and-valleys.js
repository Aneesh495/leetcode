/**
 * @param {number[]} nums
 * @return {number}
 */
var peakValleyDifference = function(nums) {
    let difference = 0;
    for (let i = 1; i + 1 < nums.length; i++) {
        const value = nums[i];
        if (value > nums[i - 1] && value > nums[i + 1]) difference += value;
        if (value < nums[i - 1] && value < nums[i + 1]) difference -= value;
    }
    return difference;
};