var countSpecialSubsequences = function(nums) {
    const mod = 1_000_000_007;
    let zeros = 0;
    let ones = 0;
    let twos = 0;

    // Doubling covers including or skipping the current value in an existing stage.
    for (const value of nums) {
        if (value === 0) {
            zeros = (2 * zeros + 1) % mod;
        } else if (value === 1) {
            ones = (2 * ones + zeros) % mod;
        } else {
            twos = (2 * twos + ones) % mod;
        }
    }
    return twos;
};