#include <bits/stdc++.h>
using namespace std;

class Solution {
    vector<int> palStart(const string& a) {
        int n = (int)a.size();
        vector<int> best(n + 1, 0);
        for (int center = 0; center < n; ++center) {
            int l = center, r = center;
            while (l >= 0 && r < n && a[l] == a[r]) {
                best[l] = max(best[l], r - l + 1);
                --l; ++r;
            }
            l = center; r = center + 1;
            while (l >= 0 && r < n && a[l] == a[r]) {
                best[l] = max(best[l], r - l + 1);
                --l; ++r;
            }
        }
        return best;
    }

public:
    int longestPalindrome(string s, string t) {
        int n = (int)s.size(), m = (int)t.size();
        string reversedT = t;
        reverse(reversedT.begin(), reversedT.end());
        vector<int> palS = palStart(s), palT = palStart(reversedT);

        int answer = 0;
        for (int v : palS) answer = max(answer, v);
        for (int v : palT) answer = max(answer, v);

        vector<vector<int>> bestS(n, vector<int>(n + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int len = 1; len <= n - i; ++len) {
                bestS[i][len] = max(bestS[i][len - 1], 2 * len + palS[i + len]);
            }
        }
        vector<vector<int>> bestT(m, vector<int>(m + 1, 0));
        for (int j = m - 1; j >= 0; --j) {
            for (int len = 1; len <= m - j; ++len) {
                bestT[j][len] = max(bestT[j][len - 1], 2 * len + palT[j + len]);
            }
        }

        vector<vector<int>> common(n + 1, vector<int>(m + 1, 0));
        for (int i = n - 1; i >= 0; --i) {
            for (int j = m - 1; j >= 0; --j) {
                if (s[i] == reversedT[j]) common[i][j] = 1 + common[i + 1][j + 1];
                int len = common[i][j];
                if (len > 0) {
                    answer = max(answer, bestS[i][len]);
                    answer = max(answer, bestT[j][len]);
                }
            }
        }
        return answer;
    }
};