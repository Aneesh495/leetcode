
var pushDominoes = function(dominoes) {
  const s = 'L' + dominoes + 'R';
  const a = s.split('');
  const res = [];
  let i = 0;
  for (let j = 1; j < a.length; j++) {
    if (a[j] === '.') continue;
    const left = a[i], right = a[j];
    const mid = j - i - 1;
    if (i > 0) res.push(left);
    if (left === right) {
      for (let k = 0; k < mid; k++) res.push(left);
    } else if (left === 'L' && right === 'R') {
      for (let k = 0; k < mid; k++) res.push('.');
    } else {
      for (let k = 0; k < Math.floor(mid / 2); k++) res.push('R');
      if (mid % 2 === 1) res.push('.');
      for (let k = 0; k < Math.floor(mid / 2); k++) res.push('L');
    }
    i = j;
  }
  return res.join('');
};
