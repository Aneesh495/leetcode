class Solution {
    public String reorderSpaces(String text) {
        int spaces = 0;
        for (int i = 0; i < text.length(); i++) {
            if (text.charAt(i) == ' ') spaces++;
        }
        String[] words = text.trim().split(" +");
        int gaps = words.length - 1;
        if (gaps == 0) return words[0] + " ".repeat(spaces);
        // Divide the spaces among gaps and place the remainder at the end.
        String separator = " ".repeat(spaces / gaps);
        return String.join(separator, words) + " ".repeat(spaces % gaps);
    }
}