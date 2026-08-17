impl Solution {
    pub fn longest_subarray(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut left = vec![1usize; n];
        let mut right = vec![1usize; n];

        for i in 1..n {
            if nums[i - 1] <= nums[i] {
                left[i] = left[i - 1] + 1;
            }
        }
        for i in (0..n.saturating_sub(1)).rev() {
            if nums[i] <= nums[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }

        let mut answer = *left.iter().max().unwrap() as usize;
        for p in 0..n {
            let l = if p > 0 { left[p - 1] } else { 0 };
            let r = if p + 1 < n { right[p + 1] } else { 0 };
            let candidate = if l > 0 && r > 0 {
                if nums[p - 1] <= nums[p + 1] { l + 1 + r }
                else { l.max(r) + 1 }
            } else {
                l + r + 1
            };
            answer = answer.max(candidate);
        }
        answer as i32
    }
}