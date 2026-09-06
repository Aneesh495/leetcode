/**
 * @param {number[][]} lists
 * @return {number}
 */
var minMergeCost = function(lists) {
    const n = lists.length;
    const states = 1 << n;
    const totalLength = new Array(states).fill(0);
    const median = new Array(states).fill(0);
    const values = [...new Set(lists.flat())].sort((a, b) => a - b);
    const upperBound = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    for (let mask = 1; mask < states; mask++) {
        const bit = mask & -mask;
        const idx = 31 - Math.clz32(bit);
        totalLength[mask] = totalLength[mask ^ bit] + lists[idx].length;
    }
    for (let mask = 1; mask < states; mask++) {
        const rank = Math.ceil(totalLength[mask] / 2);
        let lo = 0, hi = values.length - 1;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            let count = 0;
            for (let i = 0; i < n; i++) {
                if (mask & (1 << i)) count += upperBound(lists[i], values[mid]);
            }
            if (count >= rank) hi = mid;
            else lo = mid + 1;
        }
        median[mask] = values[lo];
    }
    const dp = new Array(states).fill(Infinity);
    dp[0] = 0;
    for (let i = 0; i < n; i++) dp[1 << i] = 0;
    for (let mask = 1; mask < states; mask++) {
        const firstBit = mask & -mask;
        for (let left = (mask - 1) & mask; left; left = (left - 1) & mask) {
            if (!(left & firstBit)) continue;
            const right = mask ^ left;
            if (right === 0) continue;
            const cost = totalLength[mask] + Math.abs(median[left] - median[right]);
            dp[mask] = Math.min(dp[mask], dp[left] + dp[right] + cost);
        }
    }
    return dp[states - 1];
};