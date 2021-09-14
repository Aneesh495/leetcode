class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        int rows[3] = {}, cols[3] = {}, d = 0, e = 0;
        for (int i = 0; i < moves.size(); ++i) {
            int r = moves[i][0], c = moves[i][1], v = i % 2 ? -1 : 1;
            rows[r] += v; cols[c] += v;
            if (r == c) d += v;
            if (r + c == 2) e += v;
            if (abs(rows[r]) == 3 || abs(cols[c]) == 3 || abs(d) == 3 || abs(e) == 3) return v == 1 ? "A" : "B";
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};