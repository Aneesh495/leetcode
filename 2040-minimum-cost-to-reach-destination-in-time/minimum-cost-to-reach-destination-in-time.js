/**
 * @param {number} maxTime
 * @param {number[][]} edges
 * @param {number[]} passingFees
 * @return {number}
 */
var minCost = function(maxTime, edges, passingFees) {
    const n = passingFees.length;
    const dp = Array.from({ length: maxTime + 1 }, () => new Int32Array(n).fill(1e9));
    dp[0][0] = passingFees[0];

    for (let time = 0; time <= maxTime; time++) {
        for (const [u, v, travel] of edges) {
            const nextTime = time + travel;
            if (nextTime > maxTime) continue;
            if (dp[time][u] < 1e9) {
                dp[nextTime][v] = Math.min(dp[nextTime][v], dp[time][u] + passingFees[v]);
            }
            if (dp[time][v] < 1e9) {
                dp[nextTime][u] = Math.min(dp[nextTime][u], dp[time][v] + passingFees[u]);
            }
        }
    }

    let answer = 1e9;
    for (let time = 0; time <= maxTime; time++) {
        answer = Math.min(answer, dp[time][n - 1]);
    }
    return answer === 1e9 ? -1 : answer;
};