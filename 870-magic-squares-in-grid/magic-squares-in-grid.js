
var numMagicSquaresInside = function(grid) {
  const R = grid.length, C = grid[0].length;
  if (R < 3 || C < 3) return 0;

  const isMagic = (r, c) => {
    // check values 1..9 and uniqueness
    const seen = new Array(10).fill(false);
    for (let i = r; i < r + 3; i++) {
      for (let j = c; j < c + 3; j++) {
        const v = grid[i][j];
        if (v < 1 || v > 9 || seen[v]) return false;
        seen[v] = true;
      }
    }

    // quick property: center must be 5
    if (grid[r + 1][c + 1] !== 5) return false;

    const s1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2];
    const s2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2];
    const s3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2];
    if (s1 !== 15 || s2 !== 15 || s3 !== 15) return false;

    const c1 = grid[r][c] + grid[r + 1][c] + grid[r + 2][c];
    const c2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1];
    const c3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2];
    if (c1 !== 15 || c2 !== 15 || c3 !== 15) return false;

    const d1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2];
    const d2 = grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c];
    return d1 === 15 && d2 === 15;
  };

  let count = 0;
  for (let i = 0; i + 2 < R; i++) {
    for (let j = 0; j + 2 < C; j++) {
      if (isMagic(i, j)) count++;
    }
  }
  return count;
};
