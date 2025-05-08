class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        double tot = 0, lo = 1e9, hi = 0;
        for (auto& s : squares) {
            double y = s[1], l = s[2];
            tot += l * l;
            lo = min(lo, y);
            hi = max(hi, y + l);
        }
        for (int it = 0; it < 60; ++it) {
            double mid = (lo + hi) * 0.5;
            double below = 0;
            for (auto& s : squares) {
                double y = s[1], l = s[2];
                if (y < mid) below += l * min(l, mid - y);
            }
            if (below * 2.0 >= tot) hi = mid;
            else lo = mid;
        }
        return hi;
    }
};