/**
 * @param {string} s
 * @return {number}
 */
var countValidSubstrings = function(s) {
    let latestA = -1;
    let latestAB = -1;
    let forbiddenThrough = -1;
    let total = 0;
    for (let end = 0; end < s.length; end++) {
        if (s[end] === 'a') latestA = end;
        else if (s[end] === 'b') latestAB = latestA;
        else forbiddenThrough = latestAB;
        // Every start after the latest completed abc's a is still valid.
        total += end - forbiddenThrough;
    }
    return total;
};