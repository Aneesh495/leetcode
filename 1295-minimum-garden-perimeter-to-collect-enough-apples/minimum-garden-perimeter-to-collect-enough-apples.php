class Solution {
    /**
     * @param Integer $neededApples
     * @return Integer
     */
    function minimumPerimeter($neededApples) {
        $low = 0;
        $high = 1;
        while (2 * $high * ($high + 1) * (2 * $high + 1) < $neededApples) {
            $high *= 2;
        }
        while ($low < $high) {
            $mid = intdiv($low + $high, 2);
            if (2 * $mid * ($mid + 1) * (2 * $mid + 1) >= $neededApples) {
                $high = $mid;
            } else {
                $low = $mid + 1;
            }
        }
        return 8 * $low;
    }
}