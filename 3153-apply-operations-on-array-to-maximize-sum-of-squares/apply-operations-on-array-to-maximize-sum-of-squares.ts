function maxSum(nums: number[], k: number): number {
    const counts = Array(31).fill(0);
    for (const value of nums) {
        for (let bit = 0; bit < 31; bit++) {
            if ((value & (1 << bit)) !== 0) counts[bit]++;
        }
    }
    const mod = 1000000007n;
    let answer = 0n;
    for (let i = 0; i < k; i++) {
        let value = 0;
        for (let bit = 0; bit < 31; bit++) {
            if (counts[bit] > 0) {
                value += 2 ** bit;
                counts[bit]--;
            }
        }
        const bigValue = BigInt(value);
        answer = (answer + bigValue * bigValue) % mod;
    }
    return Number(answer);
}