class Solution {
public:
    int maxRepOpt1(string text) {
        vector<int> total(26, 0);
        for (char c : text)
            total[c - 'a']++;

        int ans = 0;

        for (char ch = 'a'; ch <= 'z'; ch++) {
            int l = 0, diff = 0;

            for (int r = 0; r < text.size(); r++) {
                if (text[r] != ch)
                    diff++;

                while (diff > 1) {
                    if (text[l] != ch)
                        diff--;
                    l++;
                }

                int windowLen = r - l + 1;
                ans = max(ans, min(windowLen, total[ch - 'a']));
            }
        }

        return ans;
    }
};