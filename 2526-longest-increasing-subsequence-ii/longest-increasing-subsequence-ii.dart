class Solution {
  int lengthOfLIS(List<int> nums, int k) {
    int maxValue = nums[0];
    for (final x in nums) {
      if (x > maxValue) maxValue = x;
    }
    int size = 1;
    while (size <= maxValue) {
      size <<= 1;
    }
    final tree = List<int>.filled(size * 2, 0);

    int query(int left, int right) {
      int best = 0;
      left += size;
      right += size;
      while (left <= right) {
        if ((left & 1) == 1) {
          if (tree[left] > best) best = tree[left];
          left++;
        }
        if ((right & 1) == 0) {
          if (tree[right] > best) best = tree[right];
          right--;
        }
        left >>= 1;
        right >>= 1;
      }
      return best;
    }

    void update(int position, int value) {
      int index = position + size;
      if (tree[index] >= value) return;
      tree[index] = value;
      index >>= 1;
      while (index > 0) {
        final next = tree[index * 2] > tree[index * 2 + 1] ? tree[index * 2] : tree[index * 2 + 1];
        if (tree[index] == next) break;
        tree[index] = next;
        index >>= 1;
      }
    }

    int answer = 0;
    for (final x in nums) {
      final left = x - k > 1 ? x - k : 1;
      final right = x - 1;
      final length = 1 + (left <= right ? query(left, right) : 0);
      update(x, length);
      if (length > answer) answer = length;
    }
    return answer;
  }
}