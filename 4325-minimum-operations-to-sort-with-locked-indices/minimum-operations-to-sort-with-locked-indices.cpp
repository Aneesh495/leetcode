class Solution {
public:
    int minOperations(vector<int>& nums, vector<int>& locked, int k) {
        const int n = nums.size();
        vector<bool> needsAccess(n);
        int prefixMax = 0;
        for (int i = 0; i + 1 < n; ++i) {
            prefixMax = max(prefixMax, nums[i]);
            // A value belonging beyond this cut must cross its adjacent edge.
            if (prefixMax > i + 1) needsAccess[i] = needsAccess[i + 1] = true;
        }
        int unlocks = 0;
        for (int i = 0; i < n; ++i) unlocks += needsAccess[i] && locked[i];
        if (unlocks > k) return -1;

        vector<int> fenwick(n + 1);
        long long swaps = 0;
        for (int i = 0; i < n; ++i) {
            int smaller = 0;
            for (int p = nums[i]; p > 0; p -= p & -p) smaller += fenwick[p];
            swaps += i - smaller;
            for (int p = nums[i]; p <= n; p += p & -p) ++fenwick[p];
        }
        // Each inversion takes one adjacent swap within an unlocked component.
        return swaps + unlocks;
    }
};