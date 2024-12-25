function areSimilar(mat: number[][], k: number): boolean {
    const rows = mat.length;
    const cols = mat[0].length;
    const shift = k % cols;
    for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
            const source = r % 2 === 0
                ? (c + shift) % cols
                : (c - shift + cols) % cols;
            if (mat[r][c] !== mat[r][source]) return false;
        }
    }
    return true;
}