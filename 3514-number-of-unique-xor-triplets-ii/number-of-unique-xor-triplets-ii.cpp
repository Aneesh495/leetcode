class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        bitset<2048> p2, p3;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i; j < n; ++j) p2.set(nums[i] ^ nums[j]);
        }
        for (int x = 0; x < 2048; ++x) if (p2[x]) {
            for (int v : nums) p3.set(x ^ v);
        }
        return p3.count();
    }
};