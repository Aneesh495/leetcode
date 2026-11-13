class Solution {
public:
    int countStaircase(vector<int>& nums) {
        const int n = nums.size();
        vector<vector<int>> positions(100001);
        vector<int> ordinal(n);
        set<int> firstOccurrence;
        for (int i = 0; i < n; ++i) {
            auto& occurrences = positions[nums[i]];
            ordinal[i] = occurrences.size();
            if (occurrences.empty()) firstOccurrence.insert(i);
            occurrences.push_back(i);
        }

        long long answer = 0;
        for (int start = 0; start < n; ++start) {
            int length = 0, rank = 0;
            int minimumEnd = start, maximumEnd = n;
            for (int index : firstOccurrence) {
                length += ++rank;
                if (start + length > n || index >= maximumEnd) break;
                const auto& occurrences = positions[nums[index]];
                int needed = ordinal[index] + rank - 1;
                if (needed >= occurrences.size()) break;
                minimumEnd = max(minimumEnd, occurrences[needed]);
                if (needed + 1 < occurrences.size()) maximumEnd = min(maximumEnd, occurrences[needed + 1]);
                if (minimumEnd >= maximumEnd) break;
                // Required frequencies sum to length, leaving no room for any unseen value.
                int end = start + length - 1;
                if (minimumEnd <= end && end < maximumEnd) ++answer;
            }
            firstOccurrence.erase(start);
            const auto& occurrences = positions[nums[start]];
            if (ordinal[start] + 1 < occurrences.size()) firstOccurrence.insert(occurrences[ordinal[start] + 1]);
        }
        return answer;
    }
};