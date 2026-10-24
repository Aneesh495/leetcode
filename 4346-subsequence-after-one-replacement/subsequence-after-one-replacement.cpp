class Solution {
public:
    bool canMakeSubsequence(string s, string t) {
        int exact = 0, allowed = 0;
        for (char c : t) {
            // Replace the next character after an exact prefix, or extend a prefix already using an edit.
            int extended = max(exact + 1, allowed + (s[allowed] == c));
            if (s[exact] == c) ++exact;
            allowed = extended;
            if (allowed == s.size()) return true;
        }
        return false;
    }
};