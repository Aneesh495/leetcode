class Solution {
    func minTime(_ skill: [Int], _ mana: [Int]) -> Int {
        let n = skill.count
        var prefix = Array(repeating: 0, count: n)
        prefix[0] = skill[0]
        if n > 1 {
            for i in 1..<n { prefix[i] = prefix[i - 1] + skill[i] }
        }
        var start = 0
        for potion in 1..<mana.count {
            var delay = 0
            for wizard in 0..<n {
                let before = wizard == 0 ? 0 : prefix[wizard - 1]
                delay = max(delay, prefix[wizard] * mana[potion - 1] - before * mana[potion])
            }
            start += delay
        }
        return start + prefix[n - 1] * mana[mana.count - 1]
    }
}