impl Solution {
    pub fn minimum_deletions(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut min_index = 0;
        let mut max_index = 0;
        for i in 1..n {
            if nums[i] < nums[min_index] { min_index = i; }
            if nums[i] > nums[max_index] { max_index = i; }
        }
        let left = min_index.min(max_index);
        let right = min_index.max(max_index);
        (right + 1).min(n - left).min(left + 1 + n - right) as i32
    }
}