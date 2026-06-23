class Solution {
public:
    int maxValidSplits(vector<int>& nums) {
        const int n = nums.size();
        vector<int> prefix(n + 1), suffix(n + 1);
        for (int i = 0; i < n; ++i) prefix[i + 1] = gcd(prefix[i], nums[i]);
        for (int i = n - 1; i >= 0; --i) suffix[i] = gcd(suffix[i + 1], nums[i]);
        vector<vector<int>> table{nums};
        for (int size = 2; size <= n; size *= 2) {
            const auto& previous = table.back();
            vector<int> layer(n - size + 1);
            for (int i = 0; i < layer.size(); ++i) layer[i] = gcd(previous[i], previous[i + size / 2]);
            table.push_back(move(layer));
        }
        auto range = [&](int left, int right) {
            if (left == right) return 0;
            int level = 31 - __builtin_clz(static_cast<unsigned>(right - left));
            return gcd(table[level][left], table[level][right - (1 << level)]);
        };

        int best = 0;
        for (int removed = -1; removed < n; ++removed) {
            int length = n - (removed >= 0);
            int overall = removed < 0 ? prefix[n] : gcd(prefix[removed], suffix[removed + 1]);
            auto first = [&](bool fromLeft) {
                int low = 1, high = length;
                while (low < high) {
                    int count = (low + high) / 2;
                    int value;
                    if (fromLeft) {
                        value = removed < 0 || count <= removed ? prefix[count]
                              : gcd(prefix[removed], range(removed + 1, count + 1));
                    } else {
                        value = removed < 0 || count <= n - 1 - removed ? suffix[n - count]
                              : gcd(range(n - count - 1, removed), suffix[removed + 1]);
                    }
                    if (value == overall) high = count;
                    else low = count + 1;
                }
                return low;
            };
            // A valid split must reach the whole-array GCD on both sides.
            best = max(best, length - first(true) - first(false) + 1);
        }
        return best;
    }
};