class Solution {
    fun maxTaskAssign(tasks: IntArray, workers: IntArray, pills: Int, strength: Int): Int {
        tasks.sort()
        workers.sort()
        fun canAssign(count: Int): Boolean {
            val available = java.util.ArrayDeque<Int>()
            var taskIndex = 0
            var pillsUsed = 0
            for (workerIndex in workers.size - count until workers.size) {
                val worker = workers[workerIndex]
                while (taskIndex < count && tasks[taskIndex] <= worker + strength) {
                    available.addLast(tasks[taskIndex])
                    taskIndex++
                }
                if (available.isEmpty()) return false
                if (available.peekFirst() <= worker) {
                    available.removeFirst()
                } else {
                    if (pillsUsed == pills) return false
                    pillsUsed++
                    available.removeLast()
                }
            }
            return true
        }
        var low = 0
        var high = minOf(tasks.size, workers.size)
        while (low < high) {
            val mid = low + (high - low + 1) / 2
            if (canAssign(mid)) low = mid else high = mid - 1
        }
        return low
    }
}