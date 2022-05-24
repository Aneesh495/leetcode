public class Solution {
    public int MinimumMountainRemovals(int[] nums) {
        int n = nums.Length;
        int[] increasing = new int[n];
        int[] decreasing = new int[n];
        Array.Fill(increasing, 1);
        Array.Fill(decreasing, 1);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) increasing[i] = Math.Max(increasing[i], increasing[j] + 1);
            }
        }
        for (int i = n - 1; i >= 0; i--) {
            for (int j = i + 1; j < n; j++) {
                if (nums[j] < nums[i]) decreasing[i] = Math.Max(decreasing[i], decreasing[j] + 1);
            }
        }

        int longest = 0;
        for (int i = 1; i < n - 1; i++) {
            if (increasing[i] > 1 && decreasing[i] > 1) {
                longest = Math.Max(longest, increasing[i] + decreasing[i] - 1);
            }
        }
        return n - longest;
    }
}