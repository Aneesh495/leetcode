
class Solution {
public:
    int largestValsFromLabels(vector<int>& values, vector<int>& labels, int numWanted, int useLimit) {
        vector<pair<int, int>> items;
        for (int i = 0; i < values.size(); ++i)
            items.push_back({values[i], labels[i]});
        sort(items.rbegin(), items.rend());
        unordered_map<int, int> used;
        int sum = 0, count = 0;
        for (auto& [v, l] : items) {
            if (used[l] < useLimit) {
                sum += v;
                used[l]++;
                if (++count == numWanted) break;
            }
        }
        return sum;
    }
};
