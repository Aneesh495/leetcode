int palindromePartition(char* s, int k) {
    int n = 0;
    while (s[n] != '\0') ++n;
    int cost[n][n];
    for (int gap = 0; gap < n; ++gap) {
        for (int i = 0, j = gap; j < n; ++i, ++j) {
            cost[i][j] = (gap > 1 ? cost[i + 1][j - 1] : 0) + (s[i] != s[j]);
        }
    }
    const int INF = 1000000;
    int prev[n + 1], cur[n + 1];
    for (int i = 0; i <= n; ++i) prev[i] = INF;
    prev[0] = 0;
    for (int parts = 1; parts <= k; ++parts) {
        for (int i = 0; i <= n; ++i) cur[i] = INF;
        for (int end = parts; end <= n; ++end) {
            for (int split = parts - 1; split < end; ++split) {
                int candidate = prev[split] + cost[split][end - 1];
                if (candidate < cur[end]) cur[end] = candidate;
            }
        }
        for (int i = 0; i <= n; ++i) prev[i] = cur[i];
    }
    return prev[n];
}