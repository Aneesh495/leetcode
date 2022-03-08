class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var increments = 0
        var maxBits = 0
        for number in nums {
            var value = number
            var bits = 0
            while value > 0 {
                if (value & 1) == 1 { increments += 1 }
                value >>= 1
                bits += 1
            }
            maxBits = max(maxBits, bits)
        }
        return increments + max(0, maxBits - 1)
    }
}