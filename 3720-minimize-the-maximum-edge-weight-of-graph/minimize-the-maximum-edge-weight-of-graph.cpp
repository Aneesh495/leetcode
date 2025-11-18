class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        vector<vector<pair<int, int>>> reversed(n);
        for (const auto& edge : edges)
            reversed[edge[1]].push_back({edge[0], edge[2]});
        vector<int> best(n, INT_MAX);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        best[0] = 0;
        pq.push({0, 0});
        while (!pq.empty()) {
            auto [cost, node] = pq.top();
            pq.pop();
            if (cost != best[node]) continue;
            for (auto [next, weight] : reversed[node]) {
                int candidate = max(cost, weight);
                if (candidate < best[next]) {
                    best[next] = candidate;
                    pq.push({candidate, next});
                }
            }
        }
        int answer = 0;
        for (int value : best) {
            if (value == INT_MAX) return -1;
            answer = max(answer, value);
        }
        return answer;
    }
};