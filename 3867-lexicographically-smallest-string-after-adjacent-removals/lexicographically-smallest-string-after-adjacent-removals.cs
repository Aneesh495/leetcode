public class Solution {
    public string LexicographicallySmallestString(string s) {
        int n = s.Length;
        bool[,] removable = new bool[n + 1, n + 1];
        for (int i = 0; i <= n; i++) removable[i, i] = true;
        for (int length = 2; length <= n; length += 2) {
            for (int left = 0; left + length <= n; left++) {
                int right = left + length;
                for (int partner = left + 1; partner < right; partner += 2) {
                    int difference = Math.Abs(s[left] - s[partner]);
                    bool consecutive = difference == 1 || difference == 25;
                    if (consecutive && removable[left + 1, partner] && removable[partner + 1, right]) {
                        removable[left, right] = true;
                        break;
                    }
                }
            }
        }
        string[] best = new string[n + 1];
        best[n] = "";
        for (int start = n - 1; start >= 0; start--) {
            string answer = removable[start, n] ? "" : null;
            for (int firstKept = start; firstKept < n; firstKept++) {
                if (!removable[start, firstKept]) continue;
                string candidate = s[firstKept] + best[firstKept + 1];
                if (answer == null || string.CompareOrdinal(candidate, answer) < 0) answer = candidate;
            }
            best[start] = answer;
        }
        return best[0];
    }
}