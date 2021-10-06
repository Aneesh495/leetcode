import scala.collection.mutable
object Solution {
    def getAncestors(n: Int, edges: Array[Array[Int]]): List[List[Int]] = {
        val graph = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
        val indegree = Array.fill(n)(0)
        for (e <- edges) {
            graph(e(0)) += e(1)
            indegree(e(1)) += 1
        }
        val ancestors = Array.fill(n)(mutable.BitSet.empty)
        val queue = mutable.Queue.empty[Int]
        for (i <- 0 until n) if (indegree(i) == 0) queue.enqueue(i)
        while (queue.nonEmpty) {
            val u = queue.dequeue()
            for (v <- graph(u)) {
                ancestors(v) ++= ancestors(u)
                ancestors(v) += u
                indegree(v) -= 1
                if (indegree(v) == 0) queue.enqueue(v)
            }
        }
        ancestors.map(_.toList.sorted).toList
    }
}