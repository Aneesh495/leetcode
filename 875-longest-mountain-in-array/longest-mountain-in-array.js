
/**
 * @param {number[]} arr
 * @return {number}
 */
var longestMountain = function(arr) {
  const n = arr.length;
  let ans = 0, i = 1;
  while (i < n - 1) {
    if (!(arr[i - 1] < arr[i] && arr[i] > arr[i + 1])) { i++; continue; }
    let l = i - 1, r = i + 1;
    while (l > 0 && arr[l - 1] < arr[l]) l--;
    while (r < n - 1 && arr[r] > arr[r + 1]) r++;
    ans = Math.max(ans, r - l + 1);
    i = r;
  }
  return ans;
};
