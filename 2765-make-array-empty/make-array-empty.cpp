class Solution {
public:
    long long countOperationsToEmptyArray(vector<int>& nums) {
        const int n = nums.size();
        vector<int> order(n);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) {
            return nums[a] < nums[b];
        });

        long long operations = n;
        // Start with one operation per element. Every wrap adds one extra
        // operation for each element that is still in the circular queue.
        for (int i = 1; i < n; ++i) {
            if (order[i] < order[i - 1]) operations += n - i;
        }
        return operations;
    }
};