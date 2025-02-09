
var largestOverlap = function(img1, img2) {
  const n = img1.length;
  const A = [], B = [];
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      if (img1[i][j] === 1) A.push([i, j]);
      if (img2[i][j] === 1) B.push([i, j]);
    }
  }
  if (A.length === 0 || B.length === 0) return 0;

  const count = new Map();
  let ans = 0;

  for (const [i1, j1] of A) {
    for (const [i2, j2] of B) {
      const key = (i1 - i2) + ',' + (j1 - j2);
      const c = (count.get(key) || 0) + 1;
      count.set(key, c);
      if (c > ans) ans = c;
    }
  }
  return ans;
};
