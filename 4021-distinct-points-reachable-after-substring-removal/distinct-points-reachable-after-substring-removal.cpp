class Solution {
public:
    int distinctPoints(string s, int k) {
        int n = s.size();
        vector<pair<int, int>> prefix(n + 1, {0, 0});
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i];
            if (s[i] == 'U') ++prefix[i + 1].second;
            else if (s[i] == 'D') --prefix[i + 1].second;
            else if (s[i] == 'L') --prefix[i + 1].first;
            else ++prefix[i + 1].first;
        }
        set<pair<int, int>> points;
        for (int start = 0; start + k <= n; ++start) {
            int removedX = prefix[start + k].first - prefix[start].first;
            int removedY = prefix[start + k].second - prefix[start].second;
            points.insert({prefix[n].first - removedX, prefix[n].second - removedY});
        }
        return points.size();
    }
};