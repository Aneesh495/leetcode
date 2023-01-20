class Solution {
public:
    int numberOfWeakCharacters(vector<vector<int>>& properties) {
        sort(properties.begin(), properties.end());
        int n = properties.size(), bestDefense = -1, weak = 0;
        for (int i = n - 1; i >= 0;) {
            int j = i;
            while (j >= 0 && properties[j][0] == properties[i][0]) --j;
            for (int k = j + 1; k <= i; ++k) {
                if (properties[k][1] < bestDefense) ++weak;
            }
            bestDefense = max(bestDefense, properties[i][1]);
            i = j;
        }
        return weak;
    }
};