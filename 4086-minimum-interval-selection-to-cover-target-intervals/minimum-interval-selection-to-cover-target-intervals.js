/**
 * @param {number[][]} availableIntervals
 * @param {number[][]} targetIntervals
 * @return {number}
 */
var minSelection = function(availableIntervals, targetIntervals) {
    availableIntervals.sort((a, b) => a[0] - b[0]);
    targetIntervals.sort((a, b) => a[0] - b[0]);
    let index = 0;
    let selected = 0;
    let covered = -Infinity;
    for (const [left, right] of targetIntervals) {
        while (covered < right) {
            const point = Math.max(left, covered);
            let furthest = -Infinity;
            // At the next point requiring coverage, take the interval reaching furthest right.
            while (index < availableIntervals.length && availableIntervals[index][0] <= point) {
                furthest = Math.max(furthest, availableIntervals[index++][1]);
            }
            if (furthest < point || (furthest === point && point < right)) return -1;
            covered = furthest;
            selected++;
        }
    }
    return selected;
};