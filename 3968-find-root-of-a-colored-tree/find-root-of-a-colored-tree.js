/**
 * @param {number[][]} edges
 * @param {string} colors
 * @return {number}
 */
var findColoredRoot = function(edges, colors) {
    const size = colors.length;
    const indegree = new Uint8Array(size);
    const children = new Uint8Array(size);
    const successor = {R: 'B', B: 'W', W: 'R'};
    for (let [a, b] of edges) {
        if (colors[a] === colors[b]) return -1;
        // The two colors force the direction of this edge.
        if (successor[colors[a]] !== colors[b]) [a, b] = [b, a];
        if (++children[a] > 2 || ++indegree[b] > 1) return -1;
    }
    return indegree.indexOf(0);
};