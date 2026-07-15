#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countSequences(vector<int>& nums, long long k) {
        int target2 = 0, target3 = 0, target5 = 0;
        while (k % 2 == 0) { ++target2; k /= 2; }
        while (k % 3 == 0) { ++target3; k /= 3; }
        while (k % 5 == 0) { ++target5; k /= 5; }
        if (k != 1) return 0;

        map<tuple<int, int, int>, long long> dp;
        dp[{0, 0, 0}] = 1;
        for (int value : nums) {
            int x = value, a = 0, b = 0, c = 0;
            while (x % 2 == 0) { ++a; x /= 2; }
            while (x % 3 == 0) { ++b; x /= 3; }
            while (x % 5 == 0) { ++c; x /= 5; }
            map<tuple<int, int, int>, long long> next;
            for (const auto& [state, ways] : dp) {
                auto [u, v, w] = state;
                next[{u + a, v + b, w + c}] += ways;
                next[{u, v, w}] += ways;
                next[{u - a, v - b, w - c}] += ways;
            }
            dp = move(next);
        }
        auto it = dp.find({target2, target3, target5});
        return it == dp.end() ? 0 : static_cast<int>(it->second);
    }
};