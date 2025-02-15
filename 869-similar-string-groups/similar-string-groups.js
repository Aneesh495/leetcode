
var numSimilarGroups = function(strs) {
  const n = strs.length;
  const parent = Array.from({ length: n }, (_, i) => i);
  const rank = Array(n).fill(0);

  const find = (x) => {
    while (parent[x] !== x) {
      parent[x] = parent[parent[x]];
      x = parent[x];
    }
    return x;
  };

  const union = (a, b) => {
    const ra = find(a), rb = find(b);
    if (ra === rb) return false;
    if (rank[ra] < rank[rb]) parent[ra] = rb;
    else if (rank[rb] < rank[ra]) parent[rb] = ra;
    else { parent[rb] = ra; rank[ra]++; }
    return true;
  };

  const isSimilar = (a, b) => {
    if (a === b) return true;
    let i1 = -1, i2 = -1, diff = 0;
    for (let i = 0; i < a.length; i++) {
      if (a[i] !== b[i]) {
        diff++;
        if (diff === 1) i1 = i;
        else if (diff === 2) i2 = i;
        else return false;
      }
    }
    return diff === 2 && a[i1] === b[i2] && a[i2] === b[i1];
  };

  let groups = n;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      if (isSimilar(strs[i], strs[j]) && union(i, j)) groups--;
    }
  }
  return groups;
};
