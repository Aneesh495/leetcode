class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.rbegin(), pizzas.rend());
        int days = pizzas.size() / 4;
        int odd = (days + 1) / 2, even = days / 2;
        long long ans = 0;
        int idx = 0;
        for (int i = 0; i < odd; ++i) ans += pizzas[idx++];
        for (int i = 0; i < even; ++i) { idx++; ans += pizzas[idx++]; }
        return ans;
    }
};