class Solution {
public:
    int shadowPairs(vector<int>& nums) {
        vector<int> keys = nums;
        sort(keys.begin(), keys.end());
        keys.erase(unique(keys.begin(), keys.end()), keys.end());
        vector<int> ranks;
        ranks.reserve(nums.size());
        for (int x : nums) ranks.push_back(lower_bound(keys.begin(), keys.end(), x) - keys.begin());
        return countPairs(ranks, 0, static_cast<int>(keys.size()) - 1);
    }

private:
    long long countPairs(const vector<int>& values, int lowRank, int highRank) {
        if (lowRank >= highRank || values.size() <= 1) return 0;
        const int middle = lowRank + (highRank - lowRank) / 2;
        const int size = values.size();
        vector<int> lower, upper;
        vector<int> lowerStack, upperStack;
        vector<int> expiryHead(size, -1), expiryNext(size, -1), blocker(size, -1);
        for (int i = 0; i < size; ++i) {
            if (values[i] <= middle) {
                lower.push_back(values[i]);
                // A greater value in the lower half invalidates these starts for every upper endpoint.
                while (!lowerStack.empty() && values[lowerStack.back()] < values[i]) {
                    int start = lowerStack.back();
                    lowerStack.pop_back();
                    expiryNext[start] = expiryHead[i];
                    expiryHead[i] = start;
                }
                lowerStack.push_back(i);
            } else {
                upper.push_back(values[i]);
                while (!upperStack.empty() && values[upperStack.back()] >= values[i]) upperStack.pop_back();
                if (!upperStack.empty()) blocker[i] = upperStack.back();
                upperStack.push_back(i);
            }
        }
        vector<int> tree(size + 1);
        auto update = [&](int index, int delta) {
            for (int p = index + 1; p <= size; p += p & -p) tree[p] += delta;
        };
        auto prefix = [&](int index) {
            int count = 0;
            for (int p = index + 1; p > 0; p -= p & -p) count += tree[p];
            return count;
        };
        int active = 0;
        long long result = 0;
        for (int i = 0; i < size; ++i) {
            for (int p = expiryHead[i]; p != -1; p = expiryNext[p]) {
                update(p, -1);
                --active;
            }
            if (values[i] <= middle) {
                update(i, 1);
                ++active;
            } else {
                // Count surviving starts after the last smaller value in the upper half.
                result += active - prefix(blocker[i]);
            }
        }
        return result + countPairs(lower, lowRank, middle) + countPairs(upper, middle + 1, highRank);
    }
};