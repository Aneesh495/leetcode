#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    int countGoodNodes(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> graph(n);
        for (auto& e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }
        vector<int> parent(n, -1), order{0}, sub(n, 1);
        for (int i = 0; i < (int)order.size(); ++i) {
            int u = order[i];
            for (int v : graph[u]) if (v != parent[u]) {
                parent[v] = u;
                order.push_back(v);
            }
        }
        int good = 0;
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i], childSize = -1;
            bool same = true;
            for (int v : graph[u]) if (parent[v] == u) {
                if (childSize == -1) childSize = sub[v];
                else if (sub[v] != childSize) same = false;
                sub[u] += sub[v];
            }
            if (same) ++good;
        }
        return good;
    }
};