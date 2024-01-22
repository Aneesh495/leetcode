/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
var firstCompleteIndex = function(arr, mat) {
    const m = mat.length, n = mat[0].length;
    const position = new Array(m * n + 1);
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) position[mat[r][c]] = [r, c];
    }
    const rows = new Array(m).fill(0);
    const cols = new Array(n).fill(0);
    for (let i = 0; i < arr.length; i++) {
        const [r, c] = position[arr[i]];
        if (++rows[r] === n || ++cols[c] === m) return i;
    }
    return -1;
};