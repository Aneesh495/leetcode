class Solution {
    func minOperations(_ logs: [String]) -> Int {
        var depth = 0
        for operation in logs {
            if operation == "../" {
                depth = max(0, depth - 1)
            } else if operation != "./" {
                depth += 1
            }
        }
        return depth
    }
}