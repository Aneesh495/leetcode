class Solution {
    public int[] findDegrees(int[][] matrix) {
        int[] degree = new int[matrix.length];
        for (int node = 0; node < matrix.length; node++) {
            for (int edge : matrix[node]) degree[node] += edge;
        }
        return degree;
    }
}