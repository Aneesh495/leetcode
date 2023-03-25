public class Solution {
    public int MinimumRefill(int[] plants, int capacityA, int capacityB) {
        int left = 0, right = plants.Length - 1;
        int waterA = capacityA, waterB = capacityB;
        int refills = 0;
        while (left < right) {
            if (waterA < plants[left]) {
                waterA = capacityA;
                ++refills;
            }
            waterA -= plants[left++];
            if (waterB < plants[right]) {
                waterB = capacityB;
                ++refills;
            }
            waterB -= plants[right--];
        }
        if (left == right && Math.Max(waterA, waterB) < plants[left]) ++refills;
        return refills;
    }
}