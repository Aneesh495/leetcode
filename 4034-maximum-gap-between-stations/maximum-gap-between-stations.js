/**
 * @param {string} skill
 * @param {string} station
 * @return {number}
 */
var maximumGap = function(skill, station) {
    const earliest = new Int32Array(skill.length);
    let j = 0;
    for (let i = 0; i < skill.length; i++) {
        while (station[j] !== skill[i]) j++;
        earliest[i] = j++;
    }
    let best = 0;
    j = station.length - 1;
    // To maximize one gap, place its prefix as early and its suffix as late as possible.
    for (let i = skill.length - 1; i > 0; i--) {
        while (station[j] !== skill[i]) j--;
        best = Math.max(best, j - earliest[i - 1]);
        j--;
    }
    return best;
};