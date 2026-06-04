/**
 * @param {string} s
 * @param {number} k
 * @return {string}
 */
var mergeCharacters = function(s, k) {
    const letters = [...s];
    while (true) {
        let remove = -1;
        for (let left = 0; left < letters.length && remove < 0; left++) {
            for (let right = left + 1; right < letters.length && right <= left + k; right++) {
                if (letters[left] === letters[right]) {
                    remove = right;
                    break;
                }
            }
        }
        if (remove < 0) return letters.join('');
        // Removing a character changes later distances, so restart from the earliest pair.
        letters.splice(remove, 1);
    }
};