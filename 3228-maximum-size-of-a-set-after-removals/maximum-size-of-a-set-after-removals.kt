class Solution {
    fun maximumSetSize(nums1: IntArray, nums2: IntArray): Int {
        val first = nums1.toSet()
        val second = nums2.toSet()
        val onlyFirst = (first - second).size
        val onlySecond = (second - first).size
        val common = (first intersect second).size
        val limit = nums1.size / 2
        val takeFirst = minOf(onlyFirst, limit)
        val takeSecond = minOf(onlySecond, limit)
        val remainingSlots = (limit - takeFirst) + (limit - takeSecond)
        return takeFirst + takeSecond + minOf(common, remainingSlots)
    }
}