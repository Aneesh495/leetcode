class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int consecutive = 0;
        for (int value : arr) {
            consecutive = (value & 1) ? consecutive + 1 : 0;
            if (consecutive == 3) return true;
        }
        return false;
    }
};