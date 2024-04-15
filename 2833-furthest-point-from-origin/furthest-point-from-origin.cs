public class Solution {
    public int FurthestDistanceFromOrigin(string moves) {
        int left = 0, right = 0, wildcards = 0;
        foreach (char move in moves) {
            if (move == 'L') left++;
            else if (move == 'R') right++;
            else wildcards++;
        }
        return Math.Abs(left - right) + wildcards;
    }
}