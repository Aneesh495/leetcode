class Solution {
public:
    int maxNumberOfAlloys(int n, int k, int budget, vector<vector<int>>& composition, vector<int>& stock, vector<int>& cost) {
        long long ans = 0;
        for (const auto& comp : composition) {
            long long l = 0, r = 2e8;
            while (l < r) {
                long long mid = l + (r - l + 1) / 2, spend = 0;
                for (int i = 0; i < n; ++i) {
                    long long need = max(0LL, mid * comp[i] - stock[i]);
                    spend += need * cost[i];
                    if (spend > budget) break;
                }
                if (spend <= budget) l = mid;
                else r = mid - 1;
            }
            ans = max(ans, l);
        }
        return ans;
    }
};
