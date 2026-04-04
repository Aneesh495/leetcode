
class Solution {
public:
    string smallestSubsequence(string s) {
        vector<int> last(26, 0);
        vector<bool> seen(26, false);
        for (int i = 0; i < s.size(); ++i) last[s[i] - 'a'] = i;
        string res = "";
        for (int i = 0; i < s.size(); ++i) {
            char c = s[i];
            if (seen[c - 'a']) continue;
            while (!res.empty() && c < res.back() && i < last[res.back() - 'a']) {
                seen[res.back() - 'a'] = false;
                res.pop_back();
            }
            res.push_back(c);
            seen[c - 'a'] = true;
        }
        return res;
    }
};
