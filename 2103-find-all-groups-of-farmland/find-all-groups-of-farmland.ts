function findFarmland(land: number[][]): number[][] {
    const m = land.length, n = land[0].length;
    const groups: number[][] = [];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (land[r][c] === 0) continue;
            if (r > 0 && land[r - 1][c] === 1) continue;
            if (c > 0 && land[r][c - 1] === 1) continue;
            let bottom = r, right = c;
            while (bottom + 1 < m && land[bottom + 1][c] === 1) bottom++;
            while (right + 1 < n && land[r][right + 1] === 1) right++;
            groups.push([r, c, bottom, right]);
        }
    }
    return groups;
};