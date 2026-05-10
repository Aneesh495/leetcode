class Solution {
public:
    vector<int> minCost(int n, vector<int>& prices, vector<vector<int>>& roads) {
        struct Edge { int to, cost, tax; };
        const int size = prices.size();
        vector<vector<Edge>> graph(size);
        for (const auto& road : roads) {
            graph[road[0]].push_back({road[1], road[2], road[3]});
            graph[road[1]].push_back({road[0], road[2], road[3]});
        }
        auto shortest = [&](int start, bool carrying) {
            constexpr long long infinity = 1LL << 55;
            vector<long long> distance(size, infinity);
            using State = pair<long long,int>;
            priority_queue<State, vector<State>, greater<State>> frontier;
            frontier.emplace(0, start);
            distance[start] = 0;
            while (!frontier.empty()) {
                auto [cost, node] = frontier.top();
                frontier.pop();
                if (cost != distance[node]) continue;
                for (const auto& edge : graph[node]) {
                    long long next = cost + 1LL * edge.cost * (carrying ? edge.tax : 1);
                    if (next >= prices[start] || next >= distance[edge.to]) continue;
                    distance[edge.to] = next;
                    frontier.emplace(next, edge.to);
                }
            }
            return distance;
        };
        vector<int> answer(prices.begin(), prices.end());
        for (int i = 0; i < size; ++i) {
            auto empty = shortest(i, false);
            auto loaded = shortest(i, true);
            // Undirected roads let us compute the loaded return distances outward from i.
            for (int j = 0; j < size; ++j) {
                long long candidate = empty[j] + loaded[j] + prices[j];
                if (candidate < answer[i]) answer[i] = candidate;
            }
        }
        return answer;
    }
};