
class Solution {
    public int longestDecomposition(String text) {
        int n = text.length(), res = 0;
        String left = "", right = "";
        for (int i = 0; i < n; ++i) {
            left += text.charAt(i);
            right = text.charAt(n - i - 1) + right;
            if (left.equals(right)) {
                res++;
                left = "";
                right = "";
            }
        }
        return res;
    }
}
