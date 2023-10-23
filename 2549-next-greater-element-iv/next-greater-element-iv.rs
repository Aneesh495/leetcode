use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut answer = vec![-1; n];
        let mut first_greater_waiting: Vec<usize> = Vec::new();
        let mut second_greater_waiting: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();

        for i in 0..n {
            while let Some(&Reverse((value, index))) = second_greater_waiting.peek() {
                if value < nums[i] {
                    second_greater_waiting.pop();
                    answer[index] = nums[i];
                } else {
                    break;
                }
            }
            while let Some(&index) = first_greater_waiting.last() {
                if nums[index] < nums[i] {
                    first_greater_waiting.pop();
                    second_greater_waiting.push(Reverse((nums[index], index)));
                } else {
                    break;
                }
            }
            first_greater_waiting.push(i);
        }
        answer
    }
}