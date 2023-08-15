var countExcellentPairs = function(nums, k) {
    const frequency = Array(31).fill(0);
    for (const value of new Set(nums)) {
        let remaining = value;
        let bits = 0;
        while (remaining !== 0) {
            remaining &= remaining - 1;
            bits++;
        }
        frequency[bits]++;
    }

    // popcount(a | b) + popcount(a & b) equals popcount(a) + popcount(b).
    let pairs = 0;
    for (let a = 1; a <= 30; a++) {
        for (let b = Math.max(1, k - a); b <= 30; b++) {
            pairs += frequency[a] * frequency[b];
        }
    }
    return pairs;
};