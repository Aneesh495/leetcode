class Solution {
    func findMaximumNumber(_ k: Int, _ x: Int) -> Int {
        let limit = Int64(k)

        func accumulatedPrice(_ number: Int64) -> Int64 {
            let length = number + 1
            var total: Int64 = 0
            var bit = x - 1
            while bit <= 60 {
                let half = Int64(1) << bit
                let cycle = half << 1
                let fullCycles = length / cycle
                let remainder = length % cycle
                var ones = fullCycles * half
                if remainder > half { ones += remainder - half }
                if ones > limit - total { return limit + 1 }
                total += ones
                bit += x
            }
            return total
        }

        var low: Int64 = 0
        var high = Int64(1) << 60
        while low < high {
            let mid = low + (high - low + 1) / 2
            if accumulatedPrice(mid) <= limit {
                low = mid
            } else {
                high = mid - 1
            }
        }
        return Int(low)
    }
}