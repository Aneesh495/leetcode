class Solution {
    public int[] countPoints(int[][] points, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            long x = queries[q][0], y = queries[q][1], r = queries[q][2];
            long radiusSquared = r * r;
            for (int[] point : points) {
                long dx = point[0] - x, dy = point[1] - y;
                if (dx * dx + dy * dy <= radiusSquared) answer[q]++;
            }
        }
        return answer;
    }
}