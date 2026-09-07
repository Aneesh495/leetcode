class Solution {
    public int minimumK(int[] nums) {
        int high = 1;
        while (true) {
            long operations = 0;
            for (int value : nums) operations += (value + (long) high - 1) / high;
            if (operations <= (long) high * high) break;
            high *= 2;
        }

        int low = 1;
        while (low < high) {
            int mid = low + (high - low) / 2;
            long operations = 0;
            for (int value : nums) {
                operations += (value + (long) mid - 1) / mid;
                if (operations > (long) mid * mid) break;
            }
            if (operations <= (long) mid * mid) high = mid;
            else low = mid + 1;
        }
        return low;
    }
}