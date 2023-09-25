class Solution {
    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function longestSubarray($nums) {
        $maximum = max($nums);
        $best = 0;
        $current = 0;
        foreach ($nums as $value) {
            if ($value === $maximum) {
                $current++;
                $best = max($best, $current);
            } else {
                $current = 0;
            }
        }
        return $best;
    }
}