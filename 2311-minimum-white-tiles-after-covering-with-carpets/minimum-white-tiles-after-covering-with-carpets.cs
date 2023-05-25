public class Solution {
    public int MinimumWhiteTiles(string floor, int numCarpets, int carpetLen) {
        int n = floor.Length;
        int[] previous = new int[n + 1];
        for (int i = n - 1; i >= 0; i--)
            previous[i] = previous[i + 1] + (floor[i] == '1' ? 1 : 0);

        for (int used = 1; used <= numCarpets; used++) {
            int[] current = new int[n + 1];
            for (int i = n - 1; i >= 0; i--) {
                int leaveVisible = (floor[i] == '1' ? 1 : 0) + current[i + 1];
                int cover = previous[Math.Min(n, i + carpetLen)];
                current[i] = Math.Min(leaveVisible, cover);
            }
            previous = current;
        }
        return previous[0];
    }
}