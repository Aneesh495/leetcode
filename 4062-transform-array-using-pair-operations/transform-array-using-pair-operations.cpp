class Solution {
public:
    bool canTransform(vector<int>& source, vector<int>& target) {
        // Any coordinate can be set by transferring its difference to a fixed last coordinate.
        return accumulate(source.begin(), source.end(), 0LL) == accumulate(target.begin(), target.end(), 0LL);
    }
};