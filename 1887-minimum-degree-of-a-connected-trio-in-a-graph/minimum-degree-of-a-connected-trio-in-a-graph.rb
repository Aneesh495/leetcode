# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_trio_degree(n, edges)
    adj = Array.new(n, 0)
    degree = Array.new(n, 0)
    edges.each do |u, v|
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        degree[u] += 1
        degree[v] += 1
    end

    order = (0...n).sort_by { |v| [degree[v], v] }
    prefix_mask = [0]
    order.each { |v| prefix_mask << (prefix_mask[-1] | (1 << v)) }

    answer = Float::INFINITY
    edges.each do |u, v|
        u -= 1
        v -= 1
        common = adj[u] & adj[v]
        next if common == 0

        low = 1
        high = n
        while low < high
            mid = (low + high) / 2
            if (common & prefix_mask[mid]) != 0
                high = mid
            else
                low = mid + 1
            end
        end
        total = degree[u] + degree[v] + degree[order[low - 1]] - 6
        answer = total if total < answer
        return 0 if answer == 0
    end
    answer == Float::INFINITY ? -1 : answer
end