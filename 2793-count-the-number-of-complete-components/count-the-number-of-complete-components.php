class Solution {
    function countCompleteComponents($n, $edges) {
        $graph = array_fill(0, $n, []);
        foreach ($edges as $edge) {
            $u = $edge[0];
            $v = $edge[1];
            $graph[$u][] = $v;
            $graph[$v][] = $u;
        }
        $visited = array_fill(0, $n, false);
        $answer = 0;
        for ($start = 0; $start < $n; ++$start) {
            if ($visited[$start]) continue;
            $stack = [$start];
            $visited[$start] = true;
            $vertices = 0;
            $degreeSum = 0;
            while (!empty($stack)) {
                $u = array_pop($stack);
                $vertices++;
                $degreeSum += count($graph[$u]);
                foreach ($graph[$u] as $v) {
                    if (!$visited[$v]) {
                        $visited[$v] = true;
                        $stack[] = $v;
                    }
                }
            }
            if ($degreeSum === $vertices * ($vertices - 1)) $answer++;
        }
        return $answer;
    }
}