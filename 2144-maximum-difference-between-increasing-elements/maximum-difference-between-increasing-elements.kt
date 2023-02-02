class Solution {
    fun maximumDifference(nums: IntArray): Int {
        var minSoFar = nums[0]
        var best = -1
        for (i in 1 until nums.size) {
            if (nums[i] > minSoFar) best = maxOf(best, nums[i] - minSoFar)
            minSoFar = minOf(minSoFar, nums[i])
        }
        return best
    }
}