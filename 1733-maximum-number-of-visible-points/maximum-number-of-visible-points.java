class Solution {
    public int visiblePoints(List<List<Integer>> points, int angle, List<Integer> location) {
        int x = location.get(0), y = location.get(1);
        int atLocation = 0;
        List<Double> angles = new ArrayList<>();
        for (List<Integer> point : points) {
            int dx = point.get(0) - x, dy = point.get(1) - y;
            if (dx == 0 && dy == 0) {
                ++atLocation;
            } else {
                double degrees = Math.toDegrees(Math.atan2(dy, dx));
                if (degrees < 0) degrees += 360.0;
                angles.add(degrees);
            }
        }
        Collections.sort(angles);
        int m = angles.size();
        List<Double> extended = new ArrayList<>(2 * m);
        extended.addAll(angles);
        for (double value : angles) extended.add(value + 360.0);
        int best = 0, right = 0;
        for (int left = 0; left < m; ++left) {
            if (right < left) right = left;
            while (right < left + m && extended.get(right) - extended.get(left) <= angle + 1e-9) {
                ++right;
            }
            best = Math.max(best, right - left);
        }
        return atLocation + best;
    }
}