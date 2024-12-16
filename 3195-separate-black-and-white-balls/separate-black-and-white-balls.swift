class Solution {
    func minimumSteps(_ s: String) -> Int {
        var whiteToCross = 0
        var swaps = 0
        for ball in s.utf8.reversed() {
            if ball == 48 {
                whiteToCross += 1
            } else {
                swaps += whiteToCross
            }
        }
        return swaps
    }
}