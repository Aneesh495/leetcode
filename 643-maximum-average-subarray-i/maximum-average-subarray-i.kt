class Solution {
    fun findMaxAverage(nums: IntArray, k: Int): Double {
        var sum = 0
        for (i in 0 until k) sum += nums[i]
        var best = sum
        for (i in k until nums.size) {
            sum += nums[i] - nums[i - k]
            best = maxOf(best, sum)
        }
        return best.toDouble() / k
    }
}