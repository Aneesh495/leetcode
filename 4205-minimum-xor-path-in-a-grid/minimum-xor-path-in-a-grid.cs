public class Solution {
    public int MinCost(int[][] grid) {
        int rows = grid.Length, cols = grid[0].Length;
        bool[,,] reachable = new bool[rows, cols, 1024];
        reachable[0, 0, grid[0][0]] = true;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (r == 0 && c == 0) continue;
                int value = grid[r][c];
                for (int x = 0; x < 1024; x++) {
                    if (r > 0 && reachable[r - 1, c, x]) reachable[r, c, x ^ value] = true;
                    if (c > 0 && reachable[r, c - 1, x]) reachable[r, c, x ^ value] = true;
                }
            }
        }
        for (int x = 0; x < 1024; x++)
            if (reachable[rows - 1, cols - 1, x]) return x;
        return -1;
    }
}