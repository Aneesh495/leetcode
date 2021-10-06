class Solution {
    func sumZero(_ n: Int) -> [Int] {
        var result: [Int] = []
        if n >= 2 {
            for x in 1...(n / 2) {
                result.append(x)
                result.append(-x)
            }
        }
        if n % 2 == 1 { result.append(0) }
        return result
    }
}