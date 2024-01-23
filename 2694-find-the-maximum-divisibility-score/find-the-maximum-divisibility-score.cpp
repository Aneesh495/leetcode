#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDivScore(vector<int>& nums, vector<int>& divisors) {
        unordered_set<int> seen;
        int bestDivisor = INT_MAX;
        int bestScore = -1;
        for (int d : divisors) {
            if (!seen.insert(d).second) continue;
            int score = 0;
            for (int x : nums) score += (x % d == 0);
            if (score > bestScore || (score == bestScore && d < bestDivisor)) {
                bestScore = score;
                bestDivisor = d;
            }
        }
        return bestDivisor;
    }
};