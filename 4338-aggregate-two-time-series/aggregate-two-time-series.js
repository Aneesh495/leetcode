/**
 * @param {number[][]} series1
 * @param {number[][]} series2
 * @return {number[][]}
 */
var aggregateTimeSeries = function(series1, series2) {
    let i = 0, j = 0;
    const result = [];
    while (i < series1.length || j < series2.length) {
        const first = series1[i];
        const second = series2[j];
        const time = Math.min(first?.[0] ?? Infinity, second?.[0] ?? Infinity);
        // Each cursor is already the first entry at or after the current timestamp.
        result.push([time, (first?.[1] ?? 0) + (second?.[1] ?? 0)]);
        if (first?.[0] === time) i++;
        if (second?.[0] === time) j++;
    }
    return result;
};