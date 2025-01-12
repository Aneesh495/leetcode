object Solution {
    def incremovableSubarrayCount(nums: Array[Int]): Int = {
        val n = nums.length
        var answer = 0
        for (left <- 0 until n) {
            for (right <- left until n) {
                var previous = Int.MinValue
                var valid = true
                var i = 0
                while (i < n && valid) {
                    if (i < left || i > right) {
                        if (nums(i) <= previous) valid = false
                        previous = nums(i)
                    }
                    i += 1
                }
                if (valid) answer += 1
            }
        }
        answer
    }
}