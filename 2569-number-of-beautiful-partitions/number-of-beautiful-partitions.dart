class Solution {
  int beautifulPartitions(String s, int k, int minLength) {
    const int mod = 1000000007;
    final int n = s.length;
    bool isPrimeAt(int i) {
      final int c = s.codeUnitAt(i);
      return c == 50 || c == 51 || c == 53 || c == 55;
    }
    if (k * minLength > n || !isPrimeAt(0) || isPrimeAt(n - 1)) return 0;
    List<int> previous = List<int>.filled(n + 1, 0);
    previous[0] = 1;
    for (int part = 1; part <= k; part++) {
      final List<int> current = List<int>.filled(n + 1, 0);
      int running = 0;
      for (int end = 1; end <= n; end++) {
        final int start = end - minLength;
        if (start >= 0 && isPrimeAt(start)) {
          running = (running + previous[start]) % mod;
        }
        if (!isPrimeAt(end - 1)) current[end] = running;
      }
      previous = current;
    }
    return previous[n];
  }
}