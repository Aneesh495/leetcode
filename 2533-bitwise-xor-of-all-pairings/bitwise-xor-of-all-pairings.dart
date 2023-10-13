class Solution {
  int xorAllNums(List<int> nums1, List<int> nums2) {
    int result = 0;
    if (nums2.length.isOdd) {
      for (final value in nums1) {
        result ^= value;
      }
    }
    if (nums1.length.isOdd) {
      for (final value in nums2) {
        result ^= value;
      }
    }
    return result;
  }
}