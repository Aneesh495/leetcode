class Solution {
    function minInsertions($s) {
        $n = strlen($s);
        $dp = array_fill(0, $n, 0);
        for ($i = $n - 1; $i >= 0; --$i) {
            $dp[$i] = 1;
            $diagonal = 0;
            for ($j = $i + 1; $j < $n; ++$j) {
                $old = $dp[$j];
                if ($s[$i] === $s[$j]) {
                    $dp[$j] = $diagonal + 2;
                } else {
                    $dp[$j] = max($dp[$j], $dp[$j - 1]);
                }
                $diagonal = $old;
            }
        }
        return $n - $dp[$n - 1];
    }
}