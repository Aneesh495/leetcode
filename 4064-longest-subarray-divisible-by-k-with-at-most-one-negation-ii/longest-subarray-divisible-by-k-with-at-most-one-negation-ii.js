/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var longestSubarray = function(nums, k) {
    const never = nums.length + 1;
    const first = new Int32Array(k).fill(never);
    const withNegation = new Int32Array(k).fill(never);
    const processed = new Int32Array(k);
    const seen = [0];
    first[0] = 0;
    let prefix = 0;
    let answer = 0;
    for (let i = 0; i < nums.length; i++) {
        const shift = ((2 * nums[i]) % k + k) % k;
        // Each shift needs to consider each observed prefix remainder only once.
        for (let j = processed[shift]; j < seen.length; j++) {
            const remainder = seen[j];
            let wanted = remainder + shift;
            if (wanted >= k) wanted -= k;
            if (first[remainder] < withNegation[wanted]) withNegation[wanted] = first[remainder];
        }
        processed[shift] = seen.length;
        prefix = ((prefix + nums[i]) % k + k) % k;
        answer = Math.max(answer, i + 1 - Math.min(first[prefix], withNegation[prefix]));
        if (first[prefix] === never) {
            first[prefix] = i + 1;
            seen.push(prefix);
        }
    }
    return answer;
};