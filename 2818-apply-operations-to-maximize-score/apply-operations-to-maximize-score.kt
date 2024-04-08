class Solution {
    fun maximumScore(nums: List<Int>, k: Int): Int {
        val n = nums.size
        val values = nums.toIntArray()
        val maxValue = values.maxOrNull()!!
        val spf = IntArray(maxValue + 1)
        for (i in 2..maxValue) {
            if (spf[i] == 0) {
                spf[i] = i
                if (i <= maxValue / i) {
                    var j = i * i
                    while (j <= maxValue) {
                        if (spf[j] == 0) spf[j] = i
                        j += i
                    }
                }
            }
        }

        val primeScore = IntArray(n)
        for (i in 0 until n) {
            var x = values[i]
            while (x > 1) {
                val p = spf[x]
                primeScore[i]++
                while (x % p == 0) x /= p
            }
        }

        val left = IntArray(n)
        val right = IntArray(n)
        val stack = IntArray(n)
        var top = -1
        for (i in 0 until n) {
            while (top >= 0 && primeScore[stack[top]] < primeScore[i]) top--
            left[i] = if (top >= 0) stack[top] else -1
            stack[++top] = i
        }
        top = -1
        for (i in n - 1 downTo 0) {
            while (top >= 0 && primeScore[stack[top]] <= primeScore[i]) top--
            right[i] = if (top >= 0) stack[top] else n
            stack[++top] = i
        }

        val order = (0 until n).toMutableList()
        order.sortByDescending { values[it] }
        val mod = 1_000_000_007L
        var remaining = k.toLong()
        var answer = 1L
        for (i in order) {
            if (remaining == 0L) break
            val count = (i - left[i]).toLong() * (right[i] - i).toLong()
            val use = minOf(remaining, count)
            var base = values[i].toLong() % mod
            var exponent = use
            var power = 1L
            while (exponent > 0) {
                if ((exponent and 1L) != 0L) power = power * base % mod
                base = base * base % mod
                exponent = exponent shr 1
            }
            answer = answer * power % mod
            remaining -= use
        }
        return answer.toInt()
    }
}