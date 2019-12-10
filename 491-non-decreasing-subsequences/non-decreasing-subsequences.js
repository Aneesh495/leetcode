
/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findSubsequences = function(nums) {
  const res = [];
  const path = [];

  // Backtrack from index "start"
  // Maintain nondecreasing order by only appending nums[i] >= last
  // Use a set per depth to avoid duplicate choices that start at the same depth
  function dfs(start) {
    if (path.length >= 2) res.push(path.slice());

    const used = new Set(); // values used at this tree level
    for (let i = start; i < nums.length; i++) {
      if (used.has(nums[i])) continue; // skip duplicate starting choices at this depth
      if (path.length === 0 || nums[i] >= path[path.length - 1]) {
        used.add(nums[i]);
        path.push(nums[i]);
        dfs(i + 1);
        path.pop();
      }
    }
  }

  dfs(0);
  return res;
};
