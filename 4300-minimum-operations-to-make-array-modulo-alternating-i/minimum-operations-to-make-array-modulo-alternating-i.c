#include <limits.h>
#include <stdlib.h>

int minOperations(int* nums, int numsSize, int k) {
    int cost[2][100] = {0};
    for (int i = 0; i < numsSize; ++i) {
        int base = nums[i] % k;
        for (int residue = 0; residue < k; ++residue) {
            int steps = abs(base - residue);
            cost[i % 2][residue] += steps < k - steps ? steps : k - steps;
        }
    }
    int best = INT_MAX;
    for (int even = 0; even < k; ++even) {
        for (int odd = 0; odd < k; ++odd) {
            if (even != odd && cost[0][even] + cost[1][odd] < best) best = cost[0][even] + cost[1][odd];
        }
    }
    return best;
}