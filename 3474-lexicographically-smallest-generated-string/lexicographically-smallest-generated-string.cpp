class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size(), L = n + m - 1;
        string w(L, '?');
        vector<bool> fixed(L, false);
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    if (w[i + j] != '?' && w[i + j] != str2[j]) return "";
                    w[i + j] = str2[j];
                    fixed[i + j] = true;
                }
            }
        }
        for (int i = 0; i < L; ++i) if (w[i] == '?') w[i] = 'a';
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'F') {
                bool eq = true;
                for (int j = 0; j < m; ++j) if (w[i + j] != str2[j]) { eq = false; break; }
                if (eq) {
                    int pos = -1;
                    for (int j = m - 1; j >= 0; --j) if (!fixed[i + j]) { pos = i + j; break; }
                    if (pos == -1) return "";
                    w[pos] = 'b';
                }
            }
        }
        return w;
    }
};