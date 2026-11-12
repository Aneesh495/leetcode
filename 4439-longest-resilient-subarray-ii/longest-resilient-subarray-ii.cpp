class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int best = 1;
        for (int left = 0; left < nums.size();) {
            const int residue = nums[left] % k;
            int right = left + 1;
            while (right < nums.size() && nums[right] % k == residue) ++right;
            // All elements must have equal residues. After deletion L-1 copies remain.
            int period = k / gcd(k, residue);
            best = max(best, 1 + (right - left - 1) / period * period);
            left = right;
        }
        return best;
    }
};