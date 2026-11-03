/**
 * @param {number} n
 * @param {number} start
 * @param {number[]} requests
 * @return {number}
 */
var elevatorRequests = function(n, start, requests) {
    const floors = requests.includes(start) ? [...requests] : [...requests, start];
    floors.sort((a, b) => a - b);
    const size = floors.length;
    const pivot = floors.indexOf(start);
    let leftCost = new Float64Array(size).fill(Infinity);
    let rightCost = new Float64Array(size).fill(Infinity);
    let nextLeft = new Float64Array(size);
    let nextRight = new Float64Array(size);
    leftCost[pivot] = rightCost[pivot] = 0;
    for (let width = 1; width < size; width++) {
        nextLeft.fill(Infinity);
        nextRight.fill(Infinity);
        const waiting = size - width;
        for (let left = Math.max(0, pivot - width + 1); left <= Math.min(pivot, size - width); left++) {
            const right = left + width - 1;
            // Between consecutive served floors, every unserved request accumulates penalty.
            if (left > 0) {
                const floor = floors[left - 1];
                nextLeft[left - 1] = Math.min(leftCost[left] + (floors[left] - floor) * waiting,
                                             rightCost[left] + (floors[right] - floor) * waiting);
            }
            if (right + 1 < size) {
                const floor = floors[right + 1];
                nextRight[left] = Math.min(leftCost[left] + (floor - floors[left]) * waiting,
                                          rightCost[left] + (floor - floors[right]) * waiting);
            }
        }
        [leftCost, nextLeft] = [nextLeft, leftCost];
        [rightCost, nextRight] = [nextRight, rightCost];
    }
    return Math.min(leftCost[0], rightCost[0]);
};