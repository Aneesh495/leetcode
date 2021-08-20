object Solution {
    def tupleSameProduct(nums: Array[Int]): Int = {
        val counts = scala.collection.mutable.HashMap.empty[Int, Long]
        var answer = 0L
        for (i <- nums.indices; j <- i + 1 until nums.length) {
            val product = nums(i) * nums(j)
            val previous = counts.getOrElse(product, 0L)
            answer += previous * 8
            counts(product) = previous + 1
        }
        answer.toInt
    }
}