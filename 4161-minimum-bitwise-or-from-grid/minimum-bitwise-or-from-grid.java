class Solution {
    public int minimumOR(int[][] grid) {
        int mask = 0;
        for (int[] row : grid) for (int value : row) mask |= value;
        for (int bit = 30; bit >= 0; bit--) {
            int candidate = mask & ~(1 << bit);
            boolean possible = true;
            for (int[] row : grid) {
                boolean found = false;
                for (int value : row) {
                    if ((value & candidate) == value) {
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    possible = false;
                    break;
                }
            }
            if (possible) mask = candidate;
        }
        return mask;
    }
}