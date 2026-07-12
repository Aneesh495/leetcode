/**
 * @param {number[]} source
 * @param {number[]} target
 * @return {number}
 */
var minQueenMoves = function(source, target) {
    const rows = Math.abs(source[0] - target[0]);
    const columns = Math.abs(source[1] - target[1]);
    if (rows === 0 && columns === 0) return 0;
    if (rows === 0 || columns === 0 || rows === columns) return 1;
    return 2;
};