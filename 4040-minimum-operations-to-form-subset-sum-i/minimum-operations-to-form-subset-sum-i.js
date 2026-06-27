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
        const next = dp.slice();
        const options = [];
        // Doubling and halving cancel when all doublings precede all halvings.
        for (let value = original, cost = 0; value <= sum; value *= 2, cost++) {
            options.push([value, cost]);
        }
        for (let value = Math.floor(original / 2), cost = 1; value > 0; value = Math.floor(value / 2), cost++) {
            if (value <= sum) options.push([value, cost]);
        }
        for (const [value, cost] of options) {
            for (let previous = 0; previous + value <= sum; previous++) {
                const candidate = dp[previous] + cost;
                const total = previous + value;
                if (candidate < next[total]) next[total] = candidate;
            }
        }
        dp = next;
    }
    return dp[sum] === impossible ? -1 : dp[sum];
};