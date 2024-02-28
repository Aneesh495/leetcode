class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int cheapest = INT_MAX;
        int second = INT_MAX;
        // Track two individual chocolates, including ties in their prices.
        for (int price : prices) {
            if (price < cheapest) {
                second = cheapest;
                cheapest = price;
            } else if (price < second) {
                second = price;
            }
        }
        int cost = cheapest + second;
        return cost <= money ? money - cost : money;
    }
};