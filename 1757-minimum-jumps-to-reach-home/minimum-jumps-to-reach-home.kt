class Solution {
    fun minimumJumps(forbidden: IntArray, a: Int, b: Int, x: Int): Int {
        val limit = maxOf(x, forbidden.maxOrNull() ?: 0) + a + b
        val blocked = BooleanArray(limit + 1)
        for (p in forbidden) if (p <= limit) blocked[p] = true
        val distance = IntArray((limit + 1) * 2) { -1 }
        val queue = IntArray(distance.size)
        var head = 0
        var tail = 0
        queue[tail++] = 0
        distance[0] = 0
        while (head < tail) {
            val state = queue[head++]
            val position = state / 2
            val wentBack = state % 2 == 1
            val steps = distance[state]
            if (position == x) return steps

            val forward = position + a
            val forwardState = forward * 2
            if (forward <= limit && !blocked[forward] && distance[forwardState] == -1) {
                distance[forwardState] = steps + 1
                queue[tail++] = forwardState
            }
            val backward = position - b
            val backwardState = backward * 2 + 1
            if (!wentBack && backward >= 0 && !blocked[backward] && distance[backwardState] == -1) {
                distance[backwardState] = steps + 1
                queue[tail++] = backwardState
            }
        }
        return -1
    }
}