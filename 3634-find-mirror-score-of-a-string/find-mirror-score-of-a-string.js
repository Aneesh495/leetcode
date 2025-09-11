var calculateScore = function(s) {
    const positions = Array.from({ length: 26 }, () => []);
    let score = 0;
    for (let index = 0; index < s.length; index++) {
        const letter = s.charCodeAt(index) - 97;
        const mirrors = positions[25 - letter];
        // The last unmatched mirror is the closest one to this index.
        if (mirrors.length > 0) {
            score += index - mirrors.pop();
        } else {
            positions[letter].push(index);
        }
    }
    return score;
};