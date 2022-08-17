class Solution {
  bool canChoose(List<List<int>> groups, List<int> nums) {
    int start = 0;
    for (final group in groups) {
      bool found = false;
      for (int i = start; i + group.length <= nums.length; i++) {
        bool matches = true;
        for (int j = 0; j < group.length; j++) {
          if (nums[i + j] != group[j]) {
            matches = false;
            break;
          }
        }
        if (matches) {
          start = i + group.length;
          found = true;
          break;
        }
      }
      if (!found) return false;
    }
    return true;
  }
}