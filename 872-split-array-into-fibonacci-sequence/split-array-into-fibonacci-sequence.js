
/**
 * @param {string} num
 * @return {number[]}
 */
var splitIntoFibonacci = function(num) {
  const res = [];
  const MAX = 2 ** 31 - 1;
  const n = num.length;

  function backtrack(idx) {
    if (idx === n) return res.length >= 3;

    let cur = 0;
    for (let i = idx; i < n; i++) {
      if (i > idx && num[idx] === '0') break; // no leading zeros
      cur = cur * 10 + (num.charCodeAt(i) - 48);
      if (cur > MAX) break;

      const m = res.length;
      if (m >= 2) {
        const sum = res[m - 1] + res[m - 2];
        if (cur < sum) continue;
        if (cur > sum) break;
      }

      res.push(cur);
      if (backtrack(i + 1)) return true;
      res.pop();
    }
    return false;
  }

  return backtrack(0) ? res : [];
};
