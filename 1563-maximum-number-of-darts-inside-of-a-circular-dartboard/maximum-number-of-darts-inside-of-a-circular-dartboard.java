class Solution {
    public int numPoints(int[][] darts, int r) {
        int n = darts.length, best = 1;
        double rr = (double) r * r;
        for (int i = 0; i < n; i++) for (int j = i+1; j < n; j++) {
            double dx = darts[j][0] - darts[i][0], dy = darts[j][1] - darts[i][1];
            double d2 = dx*dx + dy*dy;
            if (d2 == 0 || d2 > 4*rr + 1e-9) continue;
            double mx = (darts[i][0]+darts[j][0])/2.0, my = (darts[i][1]+darts[j][1])/2.0;
            double factor = Math.sqrt(Math.max(0, rr/d2 - 0.25));
            for (int sign : new int[]{-1,1}) {
                double cx = mx + sign*dy*factor, cy = my - sign*dx*factor;
                int count=0;
                for (int[] p : darts) {
                    double x=p[0]-cx, y=p[1]-cy;
                    if (x*x+y*y <= rr+1e-7) count++;
                }
                best=Math.max(best,count);
            }
        }
        return best;
    }
}