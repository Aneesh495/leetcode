class Solution {
public:
    vector<bool> validSubarrays(vector<int>& nums, int k, vector<vector<int>>& queries) {
        struct Query { int left, right, index; };
        vector<Query> order;
        for (int i = 0; i < static_cast<int>(queries.size()); ++i) {
            order.push_back({queries[i][0], queries[i][1], i});
        }
        // Mo's ordering lets neighboring queries reuse most of the same window.
        const int blockSize = max(1, static_cast<int>(nums.size() / sqrt(queries.size())));
        sort(order.begin(), order.end(), [blockSize](const Query& a, const Query& b) {
            int blockA = a.left / blockSize, blockB = b.left / blockSize;
            if (blockA != blockB) return blockA < blockB;
            return blockA % 2 == 0 ? a.right < b.right : a.right > b.right;
        });

        vector<int> frequency(100001);
        int distinct = 0, odd = 0;
        auto update = [&](int value, int delta) {
            int old = frequency[value];
            int current = old + delta;
            frequency[value] = current;
            distinct += (current > 0) - (old > 0);
            odd += (current & 1) - (old & 1);
        };

        vector<bool> answer(queries.size());
        int left = 0, right = -1;
        for (const auto& query : order) {
            while (left > query.left) update(nums[--left], 1);
            while (right < query.right) update(nums[++right], 1);
            while (left < query.left) update(nums[left++], -1);
            while (right > query.right) update(nums[right--], -1);
            answer[query.index] = distinct == k && odd == 0;
        }
        return answer;
    }
};