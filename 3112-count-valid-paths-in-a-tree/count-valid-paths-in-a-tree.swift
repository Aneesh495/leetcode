class Solution {
    func countPaths(_ n: Int, _ edges: [[Int]]) -> Int {
        var graph = Array(repeating: [Int](), count: n + 1)
        for edge in edges {
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        }
        var isPrime = Array(repeating: true, count: n + 1)
        isPrime[0] = false
        if n >= 1 { isPrime[1] = false }
        if n >= 2 {
            for p in 2...n where isPrime[p] {
                if p * p <= n {
                    var multiple = p * p
                    while multiple <= n {
                        isPrime[multiple] = false
                        multiple += p
                    }
                }
            }
        }

        var componentId = Array(repeating: -1, count: n + 1)
        var componentSizes: [Int] = []
        for start in 1...n where !isPrime[start] && componentId[start] == -1 {
            let id = componentSizes.count
            var stack = [start]
            componentId[start] = id
            var size = 0
            while let node = stack.popLast() {
                size += 1
                for next in graph[node] where !isPrime[next] && componentId[next] == -1 {
                    componentId[next] = id
                    stack.append(next)
                }
            }
            componentSizes.append(size)
        }

        var answer = 0
        if n >= 2 {
            for prime in 2...n where isPrime[prime] {
                var accumulated = 1
                for neighbor in graph[prime] where !isPrime[neighbor] {
                    let size = componentSizes[componentId[neighbor]]
                    answer += accumulated * size
                    accumulated += size
                }
            }
        }
        return answer
    }
}