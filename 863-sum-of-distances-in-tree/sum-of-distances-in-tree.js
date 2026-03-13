
var sumOfDistancesInTree = function(n, edges) {
  const g = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    g[u].push(v);
    g[v].push(u);
  }

  const count = new Array(n).fill(1);
  const res = new Array(n).fill(0);

  const post = (u, p) => {
    for (const v of g[u]) {
      if (v === p) continue;
      post(v, u);
      count[u] += count[v];
      res[u] += res[v] + count[v];
    }
  };

  const pre = (u, p) => {
    for (const v of g[u]) {
      if (v === p) continue;
      res[v] = res[u] - count[v] + (n - count[v]);
      pre(v, u);
    }
  };

  post(0, -1);
  pre(0, -1);
  return res;
};
