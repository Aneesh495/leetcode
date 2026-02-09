func assignEdgeWeights(edges [][]int) int {
    graph := make([][]int, len(edges)+2)
    for _, edge := range edges {
        a, b := edge[0], edge[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }

    type state struct { node, parent, depth int }
    stack := []state{{node: 1}}
    maxDepth := 0
    for len(stack) > 0 {
        last := len(stack)-1
        current := stack[last]
        stack = stack[:last]
        if current.depth > maxDepth { maxDepth = current.depth }
        for _, next := range graph[current.node] {
            if next != current.parent {
                stack = append(stack, state{next, current.node, current.depth+1})
            }
        }
    }

    // Every assignment to the first d-1 edges has one valid choice for the final edge.
    const mod = 1000000007
    answer := 1
    for i := 1; i < maxDepth; i++ {
        answer = (answer * 2) % mod
    }
    return answer
}