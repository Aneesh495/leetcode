class Solution {
    fun friendRequests(
        n: Int,
        restrictions: Array<IntArray>,
        requests: Array<IntArray>
    ): BooleanArray {
        val parent = IntArray(n) { it }
        fun find(x: Int): Int {
            if (parent[x] != x) parent[x] = find(parent[x])
            return parent[x]
        }
        val answer = BooleanArray(requests.size)
        for (i in requests.indices) {
            val a = find(requests[i][0])
            val b = find(requests[i][1])
            if (a == b) {
                answer[i] = true
                continue
            }
            var blocked = false
            for (restriction in restrictions) {
                val x = find(restriction[0])
                val y = find(restriction[1])
                if ((x == a && y == b) || (x == b && y == a)) {
                    blocked = true
                    break
                }
            }
            if (!blocked) {
                parent[b] = a
                answer[i] = true
            }
        }
        return answer
    }
}