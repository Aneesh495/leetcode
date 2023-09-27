class Solution {
    function minimumPartition($s, $k) {
        $n = strlen($s);
        $parts = 0;
        $i = 0;
        while ($i < $n) {
            $value = 0;
            $j = $i;
            while ($j < $n) {
                $next = $value * 10 + (int)$s[$j];
                if ($next > $k) break;
                $value = $next;
                $j++;
            }
            if ($j === $i) return -1;
            $parts++;
            $i = $j;
        }
        return $parts;
    }
}