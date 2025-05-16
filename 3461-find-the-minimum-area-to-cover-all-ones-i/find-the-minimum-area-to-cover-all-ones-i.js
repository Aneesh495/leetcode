var minimumArea = function(grid) {
    let top = grid.length, bottom = -1, left = grid[0].length, right = -1;
    for (let r = 0; r < grid.length; ++r) {
        for (let c = 0; c < grid[r].length; ++c) {
            if (grid[r][c] === 1) {
                top = Math.min(top, r); bottom = Math.max(bottom, r);
                left = Math.min(left, c); right = Math.max(right, c);
            }
        }
    }
    return (bottom - top + 1) * (right - left + 1);
};