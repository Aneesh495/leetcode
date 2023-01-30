class Solution {
    public String longestSubsequenceRepeatedK(String s, int k) {
        int[] available = new int[26];
        for (char c : s.toCharArray()) available[c - 'a']++;
        int maxLength = 0;
        for (int i = 0; i < 26; i++) {
            available[i] /= k;
            maxLength += available[i];
        }
        for (int length = maxLength; length >= 1; length--) {
            String found = search(s, k, available, length, new StringBuilder());
            if (found != null) return found;
        }
        return "";
    }

    private String search(String s, int k, int[] available, int remaining, StringBuilder path) {
        if (remaining == 0) return repeatsKTimes(s, path.toString(), k) ? path.toString() : null;
        for (int c = 25; c >= 0; c--) {
            if (available[c] == 0) continue;
            available[c]--;
            path.append((char) ('a' + c));
            String found = search(s, k, available, remaining - 1, path);
            if (found != null) return found;
            path.deleteCharAt(path.length() - 1);
            available[c]++;
        }
        return null;
    }

    private boolean repeatsKTimes(String s, String candidate, int k) {
        int matched = 0, copies = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == candidate.charAt(matched) && ++matched == candidate.length()) {
                copies++;
                matched = 0;
                if (copies == k) return true;
            }
        }
        return false;
    }
}