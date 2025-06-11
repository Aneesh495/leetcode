class Solution {
public:
    int numberOfComponents(vector<vector<int>>& properties, int k) {
        int n = properties.size();
        vector<bitset<101>> bs(n);
        for (int i = 0; i < n; ++i) for (int x : properties[i]) bs[i].set(x);
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);
        auto find = [&](auto& self, int x) -> int { return p[x] == x ? x : p[x] = self(self, p[x]); };
        int comp = n;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((int)(bs[i] & bs[j]).count() >= k) {
                    int a = find(find, i), b = find(find, j);
                    if (a != b) { p[a] = b; --comp; }
                }
            }
        }
        return comp;
    }
};