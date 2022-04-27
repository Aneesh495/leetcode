class Solution {
    fun specialArray(nums: IntArray): Int {
        for (x in 0..nums.size) {
            var count = 0
            for (value in nums) if (value >= x) count++
            if (count == x) return x
        }
        return -1
    }
}