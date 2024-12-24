/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSubarrays = function(nums, k) {
    const maximum = Math.max(...nums);
    let left = 0, occurrences = 0, answer = 0;
    for (let right = 0; right < nums.length; ++right) {
        if (nums[right] === maximum) ++occurrences;
        while (occurrences >= k) {
            answer += nums.length - right;
            if (nums[left] === maximum) --occurrences;
            ++left;
        }
    }
    return answer;
};