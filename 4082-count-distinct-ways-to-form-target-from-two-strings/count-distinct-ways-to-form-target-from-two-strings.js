/**
 * @param {string} word1
 * @param {string} word2
 * @param {string} target
 * @return {number}
 */
var interleaveCharacters = function(word1, word2, target) {
    const mod = 1000000007;
    const rows = word1.length + 1;
    const cols = word2.length + 1;
    let previous = new Uint32Array(rows * cols).fill(1);
    let current = new Uint32Array(rows * cols);
    const fromFirst = new Uint32Array(cols);
    for (const letter of target) {
        fromFirst.fill(0);
        for (let i = 0; i < rows; i++) {
            let fromSecond = 0;
            for (let j = 0; j < cols; j++) {
                const index = i * cols + j;
                // Prefix sums count every choice of the final matching index in either word.
                if (i > 0 && word1[i - 1] === letter) {
                    fromFirst[j] = (fromFirst[j] + previous[index - cols]) % mod;
                }
                if (j > 0 && word2[j - 1] === letter) {
                    fromSecond = (fromSecond + previous[index - 1]) % mod;
                }
                current[index] = (fromFirst[j] + fromSecond) % mod;
            }
        }
        [previous, current] = [current, previous];
    }
    const oneWord = word => {
        const count = new Uint32Array(target.length + 1);
        count[0] = 1;
        for (const letter of word) {
            for (let j = target.length - 1; j >= 0; j--) {
                if (target[j] === letter) count[j + 1] = (count[j + 1] + count[j]) % mod;
            }
        }
        return count[target.length];
    };
    return (previous[previous.length - 1] + 2 * mod - oneWord(word1) - oneWord(word2)) % mod;
};