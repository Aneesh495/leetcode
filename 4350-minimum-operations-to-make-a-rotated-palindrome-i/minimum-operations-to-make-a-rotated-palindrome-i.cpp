class Solution {
public:
    int minOperations(string s) {
        const int n = s.size();
        const string doubled = s + s;
        int answer = INT_MAX;
        for (int rotation = 0; rotation < n; ++rotation) {
            int cost = rotation;
            for (int left = rotation, right = rotation + n - 1; left < right; ++left, --right) {
                int difference = abs(doubled[left] - doubled[right]);
                // Increment whichever endpoint reaches the other in fewer cyclic steps.
                cost += min(difference, 26 - difference);
            }
            answer = min(answer, cost);
        }
        return answer;
    }
};