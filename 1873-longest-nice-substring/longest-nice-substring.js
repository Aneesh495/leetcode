var longestNiceSubstring = function(s) {
    let start = 0;
    let length = 0;
    for (let left = 0; left < s.length; left++) {
        let lower = 0;
        let upper = 0;
        for (let right = left; right < s.length; right++) {
            const code = s.charCodeAt(right);
            const bit = 1 << ((code | 32) - 97);
            if (code < 97) upper |= bit;
            else lower |= bit;
            // Equal masks mean each present letter appears in both cases.
            if (lower === upper && right - left + 1 > length) {
                start = left;
                length = right - left + 1;
            }
        }
    }
    return s.slice(start, start + length);
};