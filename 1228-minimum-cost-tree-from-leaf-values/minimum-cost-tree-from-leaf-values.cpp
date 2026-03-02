
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int res = 0;
        vector<int> st = {INT_MAX};
        for (int a : arr) {
            while (st.back() <= a) {
                int mid = st.back(); st.pop_back();
                res += mid * min(st.back(), a);
            }
            st.push_back(a);
        }
        while (st.size() > 2) {
            int mid = st.back(); st.pop_back();
            res += mid * st.back();
        }
        return res;
    }
};
