import kotlin.math.abs

class Solution {
    fun differenceOfDistinctValues(grid: Array<IntArray>): Array<IntArray> {
        val m = grid.size
        val n = grid[0].size
        val answer = Array(m) { IntArray(n) }

        fun process(sr: Int, sc: Int) {
            val values = ArrayList<Int>()
            var r = sr
            var c = sc
            while (r < m && c < n) {
                values.add(grid[r][c])
                r++
                c++
            }
            val left = IntArray(values.size)
            val right = IntArray(values.size)
            val seen = HashSet<Int>()
            for (i in values.indices) {
                left[i] = seen.size
                seen.add(values[i])
            }
            seen.clear()
            for (i in values.indices.reversed()) {
                right[i] = seen.size
                seen.add(values[i])
            }
            r = sr
            c = sc
            for (i in values.indices) {
                answer[r][c] = abs(left[i] - right[i])
                r++
                c++
            }
        }

        for (c in 0 until n) process(0, c)
        for (r in 1 until m) process(r, 0)
        return answer
    }
}