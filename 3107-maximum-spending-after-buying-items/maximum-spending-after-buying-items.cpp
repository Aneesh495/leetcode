class Solution {
public:
    long long maxSpending(vector<vector<int>>& values) {
        vector<int> items;
        for (const auto& shop : values)
            for (int value : shop) items.push_back(value);
        sort(items.begin(), items.end());
        long long total = 0;
        for (long long day = 1; day <= (long long)items.size(); ++day)
            total += day * items[day - 1];
        return total;
    }
};