class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        var values: [String: String] = [:]
        for pair in knowledge { values[pair[0]] = pair[1] }
        let chars = Array(s)
        var result = ""
        var i = 0
        while i < chars.count {
            if chars[i] == "(" {
                var j = i + 1
                while chars[j] != ")" { j += 1 }
                let key = String(chars[(i + 1)..<j])
                result += (values[key] ?? "?")
                i = j + 1
            } else {
                result.append(chars[i])
                i += 1
            }
        }
        return result
    }
}