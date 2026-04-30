object Solution {
    def maxTotal(value: Array[Int], limit: Array[Int]): Long = {
        val n = value.length
        val groups = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
        for (i <- value.indices) groups(limit(i)) += value(i)
        var total = 0L
        for (lim <- 1 to n) {
            val best = groups(lim).sorted(Ordering.Int.reverse).take(lim)
            total += best.iterator.map(_.toLong).sum
        }
        total
    }
}