class Solution {
public:
    int maximumGroups(vector<int>& grades) {
        int groups = 0, used = 0, n = grades.size();
        while (used + groups + 1 <= n) used += ++groups;
        return groups;
    }
};