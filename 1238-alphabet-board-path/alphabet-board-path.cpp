
class Solution {
public:
    string alphabetBoardPath(string target) {
        string res;
        int r = 0, c = 0;
        for (char ch : target) {
            int idx = ch - 'a';
            int tr = idx / 5, tc = idx % 5;
            while (r > tr) { res += 'U'; r--; }
            while (c > tc) { res += 'L'; c--; }
            while (r < tr) { res += 'D'; r++; }
            while (c < tc) { res += 'R'; c++; }
            res += '!';
        }
        return res;
    }
};
