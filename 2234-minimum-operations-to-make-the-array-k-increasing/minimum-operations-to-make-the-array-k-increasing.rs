impl Solution {
    pub fn k_increasing(arr: Vec<i32>, k: i32) -> i32 {
        let n = arr.len();
        let step = k as usize;
        let mut changes = 0;
        for start in 0..step {
            let mut tails: Vec<i32> = Vec::new();
            let mut i = start;
            while i < n {
                let value = arr[i];
                let mut left = 0;
                let mut right = tails.len();
                while left < right {
                    let mid = (left + right) / 2;
                    if tails[mid] <= value { left = mid + 1; }
                    else { right = mid; }
                }
                if left == tails.len() { tails.push(value); }
                else { tails[left] = value; }
                i += step;
            }
            let length = (n - 1 - start) / step + 1;
            changes += length - tails.len();
        }
        changes as i32
    }
}