class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int cnt[10] = {0};
        for (int d : digits) cnt[d]++;
        int ans = 0;
        for (int x = 100; x <= 998; x += 2) {
            int a = x / 100, b = (x / 10) % 10, c = x % 10;
            int need[10] = {0};
            need[a]++; need[b]++; need[c]++;
            if (need[a] <= cnt[a] && need[b] <= cnt[b] && need[c] <= cnt[c]) ++ans;
        }
        return ans;
    }
};