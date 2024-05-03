function longestAlternatingSubarray(nums: number[], threshold: number): number {
    let best = 0;
    for (let start = 0; start < nums.length; start++) {
        if (nums[start] > threshold || nums[start] % 2 !== 0) continue;
        let end = start;
        while (end < nums.length && nums[end] <= threshold &&
               (end === start || nums[end] % 2 !== nums[end - 1] % 2)) {
            end++;
        }
        best = Math.max(best, end - start);
    }
    return best;
}