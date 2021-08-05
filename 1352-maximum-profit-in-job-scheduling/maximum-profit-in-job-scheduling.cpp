class Solution {
public:
    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        int n = startTime.size();
        vector<array<int, 3>> jobs;
        for (int i = 0; i < n; ++i) jobs.push_back({endTime[i], startTime[i], profit[i]});
        sort(jobs.begin(), jobs.end());
        vector<int> ends, dp(n + 1);
        for (auto& job : jobs) ends.push_back(job[0]);
        for (int i = 0; i < n; ++i) {
            int j = upper_bound(ends.begin(), ends.begin() + i, jobs[i][1]) - ends.begin();
            dp[i + 1] = max(dp[i], dp[j] + jobs[i][2]);
        }
        return dp[n];
    }
};