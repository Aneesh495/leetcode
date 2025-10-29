class Solution {
    func numberOfSubsequences(_ nums: [Int]) -> Int {
        let n = nums.count
        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let remainder = x % y
                x = y
                y = remainder
            }
            return x
        }
        func ratioKey(_ numerator: Int, _ denominator: Int) -> Int {
            let divisor = gcd(numerator, denominator)
            return (numerator / divisor) * 1001 + denominator / divisor
        }

        var leftFrequency: [Int: Int] = [:]
        var answer = 0
        for r in 0..<n {
            let q = r - 2
            if q >= 2 {
                for p in 0...(q - 2) {
                    let key = ratioKey(nums[p], nums[q])
                    leftFrequency[key, default: 0] += 1
                }
            }
            if r + 2 < n {
                for s in (r + 2)..<n {
                    answer += leftFrequency[ratioKey(nums[s], nums[r])] ?? 0
                }
            }
        }
        return answer
    }
}