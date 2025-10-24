#include <stdlib.h>
#include <limits.h>

static int *gHead, *gTo, *gWeight, *gNext, *gNums, *gLastDepth;
static long long *gPathDistance;
static int gEdgeIndex, gBestLength, gFewestNodes;

static void addEdge(int u, int v, int w) {
    gTo[gEdgeIndex] = v;
    gWeight[gEdgeIndex] = w;
    gNext[gEdgeIndex] = gHead[u];
    gHead[u] = gEdgeIndex++;
}

static void dfs(int node, int parent, int depth, long long distance, int leftDepth) {
    int value = gNums[node];
    int previousDepth = gLastDepth[value];
    int nextLeft = leftDepth;
    if (previousDepth + 1 > nextLeft) nextLeft = previousDepth + 1;
    gLastDepth[value] = depth;
    gPathDistance[depth] = distance;

    int length = (int)(distance - gPathDistance[nextLeft]);
    int nodeCount = depth - nextLeft + 1;
    if (length > gBestLength) {
        gBestLength = length;
        gFewestNodes = nodeCount;
    } else if (length == gBestLength && nodeCount < gFewestNodes) {
        gFewestNodes = nodeCount;
    }

    for (int e = gHead[node]; e != -1; e = gNext[e]) {
        int child = gTo[e];
        if (child != parent) {
            dfs(child, node, depth + 1, distance + gWeight[e], nextLeft);
        }
    }
    gLastDepth[value] = previousDepth;
}

int* longestSpecialPath(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    gHead = (int*)malloc(n * sizeof(int));
    gTo = (int*)malloc(2 * edgesSize * sizeof(int));
    gWeight = (int*)malloc(2 * edgesSize * sizeof(int));
    gNext = (int*)malloc(2 * edgesSize * sizeof(int));
    gNums = nums;
    gLastDepth = (int*)malloc(50001 * sizeof(int));
    gPathDistance = (long long*)malloc(n * sizeof(long long));

    for (int i = 0; i < n; i++) gHead[i] = -1;
    for (int i = 0; i <= 50000; i++) gLastDepth[i] = -1;
    gEdgeIndex = 0;
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], w = edges[i][2];
        addEdge(u, v, w);
        addEdge(v, u, w);
    }

    gBestLength = -1;
    gFewestNodes = INT_MAX;
    dfs(0, -1, 0, 0, 0);

    int* result = (int*)malloc(2 * sizeof(int));
    result[0] = gBestLength;
    result[1] = gFewestNodes;
    *returnSize = 2;

    free(gHead); free(gTo); free(gWeight); free(gNext);
    free(gLastDepth); free(gPathDistance);
    return result;
}