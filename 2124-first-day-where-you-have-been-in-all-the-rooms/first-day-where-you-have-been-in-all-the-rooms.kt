class Solution {
    fun firstDayBeenInAllRooms(nextVisit: IntArray): Int {
        val mod = 1_000_000_007L
        val dp = LongArray(nextVisit.size)
        for (i in 0 until nextVisit.size - 1) {
            dp[i + 1] = (2 * dp[i] - dp[nextVisit[i]] + 2 + mod) % mod
        }
        return dp.last().toInt()
    }
}