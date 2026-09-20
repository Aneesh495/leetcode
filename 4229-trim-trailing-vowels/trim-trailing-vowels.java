class Solution {
    public String trimTrailingVowels(String s) {
        int end = s.length();
        while (end > 0 && "aeiou".indexOf(s.charAt(end - 1)) >= 0) {
            end--;
        }
        return s.substring(0, end);
    }
}