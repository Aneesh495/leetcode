class Solution {
public:
    vector<string> assignUmbrella(vector<int>& rain) {
        int n = rain.size(), a = 0, b = 0;
        vector<string> ans(n);
        for (int i = 0; i < n; ++i) {
            bool na = (i + 1 < n && rain[i] == 1 && rain[i + 1] == 1);
            bool nb = (rain[i] == 1);
            if (!na && !nb) ans[i] = "None";
            else if (na && !nb) { ans[i] = "Alice"; a++; }
            else if (!na && nb) { ans[i] = "Bob"; b++; }
            else if (a <= b) { ans[i] = "Alice"; a++; }
            else { ans[i] = "Bob"; b++; }
        }
        return ans;
    }
};