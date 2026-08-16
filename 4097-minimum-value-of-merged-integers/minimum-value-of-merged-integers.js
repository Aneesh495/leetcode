/**
 * @param {number[]} nums
 * @return {number}
 */
var minMergedInteger = function(nums) {
    let answer = Infinity;
    for (let i = 0; i < nums.length; i += 2) {
        const merged = Number(String(nums[i]) + String(nums[i + 1]));
        answer = Math.min(answer, merged);
    }
    return answer;
};