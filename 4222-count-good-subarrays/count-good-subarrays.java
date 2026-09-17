import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countGoodSubarrays(int[] nums) {
        int n = nums.length;
        int[] nearest = new int[30], right = new int[n];
        Arrays.fill(nearest, n);
        for (int i = n - 1; i >= 0; i--) {
            int stop = n;
            for (int bit = 0; bit < 30; bit++) {
                if ((nums[i] & (1 << bit)) == 0) stop = Math.min(stop, nearest[bit]);
                else nearest[bit] = i;
            }
            right[i] = stop;
        }
        Arrays.fill(nearest, -1);
        Map<Integer,Integer> previousEqual = new HashMap<>();
        long count = 0;
        for (int i = 0; i < n; i++) {
            int left = previousEqual.getOrDefault(nums[i], -1);
            previousEqual.put(nums[i], i);
            for (int bit = 0; bit < 30; bit++) {
                if ((nums[i] & (1 << bit)) == 0) left = Math.max(left, nearest[bit]);
                else nearest[bit] = i;
            }
            // The first matching OR value represents the subarray. Extra set bits are forbidden.
            count += (long) (i - left) * (right[i] - i);
        }
        return count;
    }
}