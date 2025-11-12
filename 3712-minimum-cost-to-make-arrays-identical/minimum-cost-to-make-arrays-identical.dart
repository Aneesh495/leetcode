class Solution {
  int minCost(List<int> arr, List<int> brr, int k) {
    int direct = 0;
    for (int i = 0; i < arr.length; i++) {
      direct += (arr[i] - brr[i]).abs();
    }

    final sortedArr = List<int>.from(arr)..sort();
    final sortedBrr = List<int>.from(brr)..sort();
    int reordered = k;
    for (int i = 0; i < arr.length; i++) {
      reordered += (sortedArr[i] - sortedBrr[i]).abs();
    }
    return direct < reordered ? direct : reordered;
  }
}