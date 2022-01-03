class Solution {
    public String arrangeWords(String text) {
        String[] words = text.toLowerCase().split(" ");
        Arrays.sort(words, Comparator.comparingInt(String::length));
        String result = String.join(" ", words);
        return Character.toUpperCase(result.charAt(0)) + result.substring(1);
    }
}