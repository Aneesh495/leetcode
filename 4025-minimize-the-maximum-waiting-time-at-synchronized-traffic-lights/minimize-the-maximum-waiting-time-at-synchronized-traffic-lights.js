/**
 * @param {number} period
 * @param {number[]} lights
 * @param {number[]} arrivalTime
 * @return {number}
 */
var minPenalty = function(period, lights, arrivalTime) {
    let green = 0;
    for (const duration of lights) green = Math.max(green, duration);
    let penalty = 0;
    // The longest green interval is at least as good for every arrival.
    for (const time of arrivalTime) {
        const phase = time % period;
        if (phase >= green) penalty = Math.max(penalty, period - phase);
    }
    return penalty;
};