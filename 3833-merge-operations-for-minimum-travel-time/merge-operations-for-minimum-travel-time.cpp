class Solution {
public:
    long long minTravelTime(int l, int n, int k, vector<int>& position, vector<int>& time) {
        const long long INF = (1LL << 60);
        vector<long long> prefix(n, 0);
        for (int i = 0; i < n; ++i) prefix[i] = time[i] + (i ? prefix[i - 1] : 0);

        vector<vector<vector<long long>>> dp(
            n, vector<vector<long long>>(n, vector<long long>(k + 1, INF)));
        dp[0][0][0] = 0;

        for (int prev = 0; prev < n; ++prev) {
            for (int curr = prev; curr < n; ++curr) {
                for (int used = 0; used <= k; ++used) {
                    long long currentCost = dp[prev][curr][used];
                    if (currentCost == INF) continue;
                    for (int next = curr + 1; next < n; ++next) {
                        int added = next - curr - 1;
                        if (used + added > k) continue;
                        long long rate = (curr == 0) ? time[0] : prefix[curr] - prefix[prev];
                        long long segment = rate * (position[next] - position[curr]);
                        dp[curr][next][used + added] = min(
                            dp[curr][next][used + added], currentCost + segment);
                    }
                }
            }
        }

        long long answer = INF;
        for (int prev = 0; prev < n; ++prev) answer = min(answer, dp[prev][n - 1][k]);
        return answer;
    }
};