/**
 * @param {string} s
 * @param {character} x
 * @param {character} y
 * @return {string}
 */
var rearrangeString = function(s, x, y) {
    let before = 0, after = 0;
    const middle = [];
    for (const letter of s) {
        if (letter === y) before++;
        else if (letter === x) after++;
        else middle.push(letter);
    }
    return y.repeat(before) + middle.join('') + x.repeat(after);
};