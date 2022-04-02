function minSubarray(nums: number[], p: number): number {
    let total = 0;
    for (const value of nums) total = (total + value) % p;
    if (total === 0) return 0;

    const lastIndex = new Map<number, number>();
    lastIndex.set(0, -1);
    let prefix = 0;
    let best = nums.length;
    for (let i = 0; i < nums.length; i++) {
        prefix = (prefix + nums[i]) % p;
        const needed = (prefix - total + p) % p;
        const previous = lastIndex.get(needed);
        if (previous !== undefined) best = Math.min(best, i - previous);
        lastIndex.set(prefix, i);
    }
    return best === nums.length ? -1 : best;
}