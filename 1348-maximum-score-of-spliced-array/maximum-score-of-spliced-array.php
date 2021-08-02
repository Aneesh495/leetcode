class Solution {
    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Integer
     */
    function maximumsSplicedArray($nums1, $nums2) {
        $sum1 = array_sum($nums1);
        $sum2 = array_sum($nums2);
        $bestGain1 = 0;
        $currentGain1 = 0;
        $bestGain2 = 0;
        $currentGain2 = 0;
        for ($i = 0; $i < count($nums1); $i++) {
            $currentGain1 = max(0, $currentGain1 + $nums2[$i] - $nums1[$i]);
            $bestGain1 = max($bestGain1, $currentGain1);
            $currentGain2 = max(0, $currentGain2 + $nums1[$i] - $nums2[$i]);
            $bestGain2 = max($bestGain2, $currentGain2);
        }
        return max($sum1 + $bestGain1, $sum2 + $bestGain2);
    }
}