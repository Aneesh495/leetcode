class Solution {
    fun minOperations(nums: IntArray): IntArray {
        val palindromes = ArrayList<Int>()
        for (value in 1..16383) {
            val bits = Integer.toBinaryString(value)
            if (bits == bits.reversed()) palindromes.add(value)
        }
        return IntArray(nums.size) { index ->
            var best = Int.MAX_VALUE
            for (palindrome in palindromes) {
                val difference = if (palindrome >= nums[index]) palindrome - nums[index] else nums[index] - palindrome
                if (difference < best) best = difference
            }
            best
        }
    }
}