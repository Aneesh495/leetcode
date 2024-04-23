var isReachableAtTime = function(sx, sy, fx, fy, t) {
    const d = Math.max(Math.abs(sx - fx), Math.abs(sy - fy));
    return d === 0 ? t !== 1 : t >= d;
};
