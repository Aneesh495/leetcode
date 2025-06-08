class Solution {
    fun beautifulNumbers(l: Int, r: Int): Int {
        fun countLength(bound: IntArray, target: Int): Long {
            var dp = Array(2) { Array(target + 1) { LongArray(target) } }
            dp[1][0][1 % target] = 1L
            for (pos in bound.indices) {
                val next = Array(2) { Array(target + 1) { LongArray(target) } }
                for (tight in 0..1) {
                    for (sum in 0..target) {
                        for (rem in 0 until target) {
                            val ways = dp[tight][sum][rem]
                            if (ways == 0L) continue
                            val low = if (pos == 0) 1 else 0
                            val high = if (tight == 1) bound[pos] else 9
                            for (digit in low..high) {
                                val newSum = sum + digit
                                if (newSum > target) continue
                                val newTight = if (tight == 1 && digit == bound[pos]) 1 else 0
                                val newRem = (rem * digit) % target
                                next[newTight][newSum][newRem] += ways
                            }
                        }
                    }
                }
                dp = next
            }
            return dp[0][target][0] + dp[1][target][0]
        }

        fun countUpTo(value: Int): Long {
            if (value <= 0) return 0L
            val digits = value.toString().map { it - '0' }.toIntArray()
            var total = 0L
            for (length in 1..digits.size) {
                val bound = if (length == digits.size) digits else IntArray(length) { 9 }
                for (sum in 1..9 * length) total += countLength(bound, sum)
            }
            return total
        }

        return (countUpTo(r) - countUpTo(l - 1)).toInt()
    }
}