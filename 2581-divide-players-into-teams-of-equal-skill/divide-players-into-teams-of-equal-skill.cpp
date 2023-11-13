class Solution {
public:
    long long dividePlayers(vector<int>& skill) {
        sort(skill.begin(), skill.end());
        int target = skill.front() + skill.back();
        long long chemistry = 0;
        for (int i = 0, j = static_cast<int>(skill.size()) - 1; i < j; ++i, --j) {
            if (skill[i] + skill[j] != target) return -1;
            chemistry += 1LL * skill[i] * skill[j];
        }
        return chemistry;
    }
};