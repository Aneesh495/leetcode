
var isNStraightHand = function(hand, groupSize) {
  const n = hand.length;
  if (n % groupSize !== 0) return false;

  const count = new Map();
  for (const x of hand) count.set(x, (count.get(x) || 0) + 1);

  const keys = Array.from(count.keys()).sort((a, b) => a - b);

  for (const k of keys) {
    const c = count.get(k) || 0;
    if (c > 0) {
      for (let i = 0; i < groupSize; i++) {
        const key = k + i;
        const have = count.get(key) || 0;
        if (have < c) return false;
        count.set(key, have - c);
      }
    }
  }
  return true;
};
