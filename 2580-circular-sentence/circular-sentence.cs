public class Solution {
    public bool IsCircularSentence(string sentence) {
        string[] words = sentence.Split(' ');
        for (int i = 0; i < words.Length; i++) {
            string current = words[i];
            string next = words[(i + 1) % words.Length];
            if (current[current.Length - 1] != next[0]) return false;
        }
        return true;
    }
}