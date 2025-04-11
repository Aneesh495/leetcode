public class Solution {
    public int FindPermutationDifference(string s, string t) {
        int[] position = new int[26];
        for (int i = 0; i < s.Length; i++) position[s[i] - 'a'] = i;
        int difference = 0;
        for (int i = 0; i < t.Length; i++) {
            difference += Math.Abs(position[t[i] - 'a'] - i);
        }
        return difference;
    }
}