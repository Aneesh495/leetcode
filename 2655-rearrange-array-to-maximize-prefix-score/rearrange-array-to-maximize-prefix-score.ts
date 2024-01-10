function maxScore(nums: number[]): number {
    nums.sort((a, b) => b - a);
    let prefix = 0;
    let score = 0;
    for (const value of nums) {
        prefix += value;
        if (prefix <= 0) break;
        score++;
    }
    return score;
}