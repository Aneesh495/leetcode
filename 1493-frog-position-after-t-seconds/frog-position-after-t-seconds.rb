# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} t
# @param {Integer} target
# @return {Float}
def frog_position(n, edges, t, target)
    graph = Array.new(n + 1) { [] }
    edges.each do |u, v|
        graph[u] << v
        graph[v] << u
    end

    queue = [[1, 0, 1.0, 0]]
    head = 0
    while head < queue.length
        node, parent, probability, depth = queue[head]
        head += 1
        children = graph[node].length - (parent == 0 ? 0 : 1)

        if node == target
            return probability if depth == t || (depth < t && children == 0)
            return 0.0
        end
        next if depth == t || children == 0

        chance = probability / children
        graph[node].each do |neighbor|
            queue << [neighbor, node, chance, depth + 1] if neighbor != parent
        end
    end
    0.0
end