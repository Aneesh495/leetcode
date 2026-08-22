/**
 * @param {string} s1
 * @param {string} s2
 * @return {string[][]}
 */
var findMismatchedSegments = function(s1, s2) {
    const result = [];
    let start = -1;
    for (let i = 0; i <= s1.length; i++) {
        if (i < s1.length && s1[i] !== s2[i]) {
            if (start === -1) start = i;
        } else if (start !== -1) {
            result.push([s1.slice(start, i), s2.slice(start, i)]);
            start = -1;
        }
    }
    return result;
};