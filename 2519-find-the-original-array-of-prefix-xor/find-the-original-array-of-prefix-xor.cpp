class Solution {
public:
    vector<int> findArray(vector<int>& pref) {
        vector<int> answer(pref.size());
        int previous = 0;
        // Taking XOR with the previous prefix cancels all earlier elements.
        for (int i = 0; i < pref.size(); ++i) {
            answer[i] = previous ^ pref[i];
            previous = pref[i];
        }
        return answer;
    }
};