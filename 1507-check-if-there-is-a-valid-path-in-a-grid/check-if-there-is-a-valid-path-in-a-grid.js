var hasValidPath = function(grid) {
    const rows = grid.length;
    const cols = grid[0].length;
    const mask = [0, 10, 5, 12, 6, 9, 3];
    const dr = [-1, 0, 1, 0];
    const dc = [0, 1, 0, -1];
    const visited = new Uint8Array(rows * cols);
    const queue = [0];
    visited[0] = 1;
    for (let front = 0; front < queue.length; front++) {
        const cell = queue[front];
        if (cell === rows * cols - 1) return true;
        const r = Math.floor(cell / cols);
        const c = cell % cols;
        for (let d = 0; d < 4; d++) {
            if ((mask[grid[r][c]] & (1 << d)) === 0) continue;
            const nr = r + dr[d];
            const nc = c + dc[d];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            const next = nr * cols + nc;
            // Both streets must open toward the shared edge.
            if (!visited[next] && (mask[grid[nr][nc]] & (1 << (d ^ 2))) !== 0) {
                visited[next] = 1;
                queue.push(next);
            }
        }
    }
    return false;
};