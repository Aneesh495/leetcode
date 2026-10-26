#include <stdlib.h>

long long weightedSum(int* parent, int parentSize, int* nums, int numsSize) {
    int n = parentSize;
    int* memory = malloc(4 * n * sizeof(*memory));
    int* head = memory;
    int* next = head + n;
    int* queue = next + n;
    int* depth = queue + n;
    for (int i = 0; i < n; ++i) head[i] = -1;
    for (int child = 1; child < n; ++child) {
        int p = parent[child];
        next[child] = head[p];
        head[p] = child;
    }
    queue[0] = 0;
    depth[0] = 1;
    int count = 1;
    for (int i = 0; i < count; ++i) {
        int node = queue[i];
        for (int child = head[node]; child != -1; child = next[child]) {
            depth[child] = depth[node] + 1;
            queue[count++] = child;
        }
    }
    // The final BFS vertex is on a deepest level, regardless of label ordering.
    int height = depth[queue[n - 1]];
    long long total = 0;
    for (int i = 0; i < n; ++i) total += (long long)nums[i] * (height - depth[i] + 1);
    free(memory);
    return total;
}