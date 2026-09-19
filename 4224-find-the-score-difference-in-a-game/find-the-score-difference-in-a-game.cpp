class Solution {
public:
    int scoreDifference(vector<int>& nums) {
        bool firstActive = true;
        int difference = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            if (nums[i] % 2 == 1) firstActive = !firstActive;
            if ((i + 1) % 6 == 0) firstActive = !firstActive;
            difference += firstActive ? nums[i] : -nums[i];
        }
        return difference;
    }
};