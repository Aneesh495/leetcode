/**
 * @param {number} n
 * @return {boolean}
 */
var winnerSquareGame = function(n) {
    const win = new Uint8Array(n + 1);
    for (let stones = 1; stones <= n; ++stones) {
        for (let root = 1; root * root <= stones; ++root) {
            if (!win[stones - root * root]) {
                win[stones] = 1;
                break;
            }
        }
    }
    return win[n] === 1;
};