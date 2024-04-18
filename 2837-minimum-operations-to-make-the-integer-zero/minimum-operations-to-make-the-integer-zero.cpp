class Solution {
public:
    int makeTheIntegerZero(int num1, int num2) {
        for (int operations = 1; operations <= 60; ++operations) {
            long long remaining = (long long)num1 - 1LL * operations * num2;
            if (remaining >= operations && __builtin_popcountll(remaining) <= operations)
                return operations;
        }
        return -1;
    }
};