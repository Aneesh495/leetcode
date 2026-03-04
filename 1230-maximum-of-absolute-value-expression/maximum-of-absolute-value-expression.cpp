
class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        // We evaluate four linear forms that cover all absolute value cases
        // For each form track min and max across indices then update answer with max - min
        int n = arr1.size();
        int ans = 0;

        // form1 = +arr1 +arr2 +i
        int mn = INT_MAX, mx = INT_MIN;
        for (int i = 0; i < n; ++i) {
            int v = arr1[i] + arr2[i] + i;
            mn = min(mn, v);
            mx = max(mx, v);
        }
        ans = max(ans, mx - mn);

        // form2 = +arr1 +arr2 -i
        mn = INT_MAX; mx = INT_MIN;
        for (int i = 0; i < n; ++i) {
            int v = arr1[i] + arr2[i] - i;
            mn = min(mn, v);
            mx = max(mx, v);
        }
        ans = max(ans, mx - mn);

        // form3 = +arr1 -arr2 +i
        mn = INT_MAX; mx = INT_MIN;
        for (int i = 0; i < n; ++i) {
            int v = arr1[i] - arr2[i] + i;
            mn = min(mn, v);
            mx = max(mx, v);
        }
        ans = max(ans, mx - mn);

        // form4 = +arr1 -arr2 -i
        mn = INT_MAX; mx = INT_MIN;
        for (int i = 0; i < n; ++i) {
            int v = arr1[i] - arr2[i] - i;
            mn = min(mn, v);
            mx = max(mx, v);
        }
        ans = max(ans, mx - mn);

        return ans;
    }
};
