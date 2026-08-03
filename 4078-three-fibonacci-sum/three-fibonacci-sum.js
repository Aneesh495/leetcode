/**
 * @param {number} n
 * @return {boolean}
 */
var threeFibonacciSum = function(n) {
    let first = 0;
    let second = 1;
    while (2 * (first + second) <= n) {
        const third = first + second;
        // The three-term sum is twice the third term.
        if (2 * third === n) return true;
        first = second;
        second = third;
    }
    return false;
};