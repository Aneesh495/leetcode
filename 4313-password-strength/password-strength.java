class Solution {
    public int passwordStrength(String password) {
        boolean[] seen = new boolean[128];
        int total = 0;
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (seen[c]) continue;
            seen[c] = true;
            if (c >= 'a' && c <= 'z') total += 1;
            else if (c >= 'A' && c <= 'Z') total += 2;
            else if (c >= '0' && c <= '9') total += 3;
            else total += 5;
        }
        return total;
    }
}