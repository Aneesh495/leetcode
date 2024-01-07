func rootCount(edges [][]int, guesses [][]int, k int) int {
    n := len(edges) + 1
    graph := make([][]int, n)
    for _, e := range edges {
        a, b := e[0], e[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }
    guessed := make(map[[2]int]bool, len(guesses))
    for _, g := range guesses {
        guessed[[2]int{g[0], g[1]}] = true
    }

    parent := make([]int, n)
    for i := range parent { parent[i] = -2 }
    parent[0] = -1
    order := []int{0}
    base := 0
    for i := 0; i < len(order); i++ {
        u := order[i]
        for _, v := range graph[u] {
            if v == parent[u] { continue }
            parent[v] = u
            order = append(order, v)
            if guessed[[2]int{u, v}] { base++ }
        }
    }

    score := make([]int, n)
    score[0] = base
    answer := 0
    if base >= k { answer++ }
    for i := 1; i < len(order); i++ {
        v, u := order[i], parent[order[i]]
        score[v] = score[u]
        if guessed[[2]int{u, v}] { score[v]-- }
        if guessed[[2]int{v, u}] { score[v]++ }
        if score[v] >= k { answer++ }
    }
    return answer
}