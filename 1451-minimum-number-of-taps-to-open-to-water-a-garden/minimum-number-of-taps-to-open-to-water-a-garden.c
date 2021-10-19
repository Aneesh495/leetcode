int minTaps(int n, int* ranges, int rangesSize) {
    int maxReach[n + 1];
    for (int i = 0; i <= n; ++i) maxReach[i] = 0;
    for (int i = 0; i <= n; ++i) {
        int left = i - ranges[i];
        int right = i + ranges[i];
        if (left < 0) left = 0;
        if (right > n) right = n;
        if (right > maxReach[left]) maxReach[left] = right;
    }
    int taps = 0, currentEnd = 0, farthest = 0;
    for (int i = 0; i <= n; ++i) {
        if (maxReach[i] > farthest) farthest = maxReach[i];
        if (i == currentEnd) {
            if (farthest == currentEnd && currentEnd < n) return -1;
            ++taps;
            currentEnd = farthest;
            if (currentEnd >= n) return taps;
        }
    }
    return -1;
}