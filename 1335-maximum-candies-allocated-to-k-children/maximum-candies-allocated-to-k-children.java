class Solution {
    public int maximumCandies(int[] candies, long k) {
        int low = 0, high = 0;
        for (int c : candies) high = Math.max(high, c);
        while (low < high) {
            int mid = low + (high - low + 1) / 2;
            long children = 0;
            for (int c : candies) children += c / mid;
            if (children >= k) low = mid;
            else high = mid - 1;
        }
        return low;
    }
}