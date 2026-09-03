class Solution {
    public int maxArea(int[][] mat) {
        int rows = mat.length, cols = mat[0].length;
        int[][] square = new int[rows + 1][cols + 1];
        for (int r = rows - 1; r >= 0; r--) {
            for (int c = cols - 1; c >= 0; c--) {
                if (mat[r][c] == 1) {
                    square[r][c] = 1 + Math.min(square[r + 1][c + 1], Math.min(square[r + 1][c], square[r][c + 1]));
                }
            }
        }
        int low = 0, high = Math.min(rows, cols);
        while (low < high) {
            int side = (low + high + 1) / 2;
            int minRow = rows, maxRow = -1, minCol = cols, maxCol = -1;
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    if (square[r][c] < side) continue;
                    minRow = Math.min(minRow, r);
                    maxRow = Math.max(maxRow, r);
                    minCol = Math.min(minCol, c);
                    maxCol = Math.max(maxCol, c);
                }
            }
            // Non-overlap requires separation by a full side on at least one axis.
            if (maxRow - minRow >= side || maxCol - minCol >= side) low = side;
            else high = side - 1;
        }
        return low * low;
    }
}