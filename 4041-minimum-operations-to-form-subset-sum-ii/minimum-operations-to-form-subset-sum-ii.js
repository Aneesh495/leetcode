/**
 * @param {number[]} nums
 * @param {number} sum
 * @return {number}
 */
var minOperations = function(nums, sum) {
    const impossible = 1000000000;
    let dp = new Int32Array(sum + 1).fill(impossible);
    dp[0] = 0;
    for (const original of nums) {
        const choices = new Map();
        // Every doubling followed by halving cancels, leaving only divisions then multiplications.
        for (let base = original, down = 0; base > 0; base = Math.floor(base / 2), down++) {
            for (let value = base, up = 0; value <= sum; value *= 2, up++) {
                const cost = down + up;
                if (cost < (choices.get(value) ?? impossible)) choices.set(value, cost);
            }
        }
        const next = dp.slice();
        for (const [value, cost] of choices) {
            for (let previous = 0; previous + value <= sum; previous++) {
                const total = previous + value;
                const candidate = dp[previous] + cost;
                if (candidate < next[total]) next[total] = candidate;
            }
        }
        dp = next;
    }
    return dp[sum] === impossible ? -1 : dp[sum];
};