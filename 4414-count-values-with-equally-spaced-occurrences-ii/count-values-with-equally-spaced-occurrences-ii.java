import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countSpecialIntegers(int[] nums) {
        Map<Integer, Trail> occurrences = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Trail trail = occurrences.get(nums[i]);
            if (trail == null) {
                occurrences.put(nums[i], new Trail(i));
            } else {
                int nextGap = i - trail.last;
                if (trail.count == 1) trail.gap = nextGap;
                else if (trail.gap != nextGap) trail.broken = true;
                trail.last = i;
                trail.count++;
            }
        }
        int result = 0;
        for (Trail trail : occurrences.values()) if (trail.count >= 3 && !trail.broken) result++;
        return result;
    }

    private static class Trail {
        int count = 1, last, gap;
        boolean broken;
        Trail(int first) { last = first; }
    }
}