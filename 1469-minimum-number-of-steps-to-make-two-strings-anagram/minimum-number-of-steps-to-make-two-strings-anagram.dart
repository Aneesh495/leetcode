class Solution {
  int minSteps(String s, String t) {
    final count = List<int>.filled(26, 0);
    for (final code in s.codeUnits) {
      count[code - 97]++;
    }
    for (final code in t.codeUnits) {
      count[code - 97]--;
    }
    int changes = 0;
    for (final difference in count) {
      if (difference > 0) changes += difference;
    }
    return changes;
  }
}