public class Solution {
    private const int Mod = 1_000_000_007;

    public int Ways(string[] pizza, int k) {
        int rows = pizza.Length, cols = pizza[0].Length;
        int[,] apples = new int[rows + 1, cols + 1];
        for (int r = rows - 1; r >= 0; --r) {
            for (int c = cols - 1; c >= 0; --c) {
                apples[r, c] = (pizza[r][c] == 'A' ? 1 : 0)
                    + apples[r + 1, c] + apples[r, c + 1] - apples[r + 1, c + 1];
            }
        }
        int[,,] memo = new int[rows, cols, k];
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                for (int cuts = 0; cuts < k; ++cuts)
                    memo[r, c, cuts] = -1;
        return Dfs(0, 0, k - 1, apples, memo, rows, cols);
    }

    private int Dfs(int r, int c, int cuts, int[,] apples, int[,,] memo, int rows, int cols) {
        if (apples[r, c] == 0) return 0;
        if (cuts == 0) return 1;
        if (memo[r, c, cuts] != -1) return memo[r, c, cuts];
        int ways = 0;
        for (int nextR = r + 1; nextR < rows; ++nextR) {
            if (apples[r, c] > apples[nextR, c])
                ways = (ways + Dfs(nextR, c, cuts - 1, apples, memo, rows, cols)) % Mod;
        }
        for (int nextC = c + 1; nextC < cols; ++nextC) {
            if (apples[r, c] > apples[r, nextC])
                ways = (ways + Dfs(r, nextC, cuts - 1, apples, memo, rows, cols)) % Mod;
        }
        return memo[r, c, cuts] = ways;
    }
}