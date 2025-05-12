class Solution {
public:
    double separateSquares(vector<vector<int>>& squares) {
        vector<int> xs;
        struct Ev { int y, x1, x2, d; };
        vector<Ev> evs;
        for (auto& s : squares) {
            xs.push_back(s[0]);
            xs.push_back(s[0] + s[2]);
            evs.push_back({s[1], s[0], s[0] + s[2], 1});
            evs.push_back({s[1] + s[2], s[0], s[0] + s[2], -1});
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        sort(evs.begin(), evs.end(), [](const Ev& a, const Ev& b) { return a.y < b.y; });
        int m = xs.size() - 1;
        vector<int> cnt(4 * m, 0);
        vector<long long> len(4 * m, 0);
        auto upd = [&](auto& self, int u, int l, int r, int ql, int qr, int d) -> void {
            if (ql <= l && r <= qr) {
                cnt[u] += d;
            } else {
                int mid = (l + r) / 2;
                if (ql <= mid) self(self, 2 * u, l, mid, ql, qr, d);
                if (qr > mid) self(self, 2 * u + 1, mid + 1, r, ql, qr, d);
            }
            if (cnt[u] > 0) len[u] = xs[r + 1] - xs[l];
            else if (l == r) len[u] = 0;
            else len[u] = len[2 * u] + len[2 * u + 1];
        };
        struct Strip { int y1, y2; long long w; };
        vector<Strip> strips;
        double tot = 0;
        for (size_t i = 0; i + 1 < evs.size(); ++i) {
            int x1 = lower_bound(xs.begin(), xs.end(), evs[i].x1) - xs.begin();
            int x2 = lower_bound(xs.begin(), xs.end(), evs[i].x2) - xs.begin() - 1;
            if (x1 <= x2) upd(upd, 1, 0, m - 1, x1, x2, evs[i].d);
            if (evs[i + 1].y > evs[i].y && len[1] > 0) {
                strips.push_back({evs[i].y, evs[i + 1].y, len[1]});
                tot += (double)(evs[i + 1].y - evs[i].y) * len[1];
            }
        }
        double half = tot * 0.5, cur = 0;
        for (auto& st : strips) {
            double area = (double)(st.y2 - st.y1) * st.w;
            if (cur + area >= half) {
                return st.y1 + (half - cur) / st.w;
            }
            cur += area;
        }
        return 0;
    }
};