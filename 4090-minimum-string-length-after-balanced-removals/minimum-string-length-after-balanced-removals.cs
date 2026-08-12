public class Solution {
    public int MinLengthAfterRemovals(string s) {
        int countA = 0;
        foreach (char c in s) {
            if (c == 'a') ++countA;
        }
        return Math.Abs(2 * countA - s.Length);
    }
}