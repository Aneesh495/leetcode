class Solution {
    fun findNumberOfLIS(nums: IntArray): Int {
        val n = nums.size
        val len = IntArray(n) { 1 }
        val count = IntArray(n) { 1 }
        var best = 1
        for (i in 0 until n) {
            for (j in 0 until i) {
                if (nums[j] < nums[i]) {
                    if (len[j] + 1 > len[i]) {
                        len[i] = len[j] + 1
                        count[i] = count[j]
                    } else if (len[j] + 1 == len[i]) {
                        count[i] += count[j]
                    }
                }
            }
            best = maxOf(best, len[i])
        }
        var result = 0
        for (i in 0 until n) if (len[i] == best) result += count[i]
        return result
    }
}