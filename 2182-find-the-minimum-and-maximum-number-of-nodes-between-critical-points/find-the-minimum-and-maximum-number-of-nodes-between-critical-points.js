var nodesBetweenCriticalPoints = function(head) {
    let first = -1;
    let last = -1;
    let minDistance = Infinity;
    let previous = head;
    let current = head.next;
    let index = 1;

    while (current && current.next) {
        const value = current.val;
        const before = previous.val;
        const after = current.next.val;
        if ((value > before && value > after) || (value < before && value < after)) {
            if (first === -1) first = index;
            if (last !== -1) minDistance = Math.min(minDistance, index - last);
            last = index;
        }
        previous = current;
        current = current.next;
        index++;
    }
    // The minimum occurs between consecutive critical points, the maximum at the ends.
    return first === last ? [-1, -1] : [minDistance, last - first];
};