function rotatedDigits(n: number): number {
    let answer = 0;
    for (let value = 1; value <= n; value++) {
        let valid = true;
        let changes = false;
        for (const digit of value.toString()) {
            if (digit === '3' || digit === '4' || digit === '7') {
                valid = false;
                break;
            }
            if (digit === '2' || digit === '5' || digit === '6' || digit === '9') changes = true;
        }
        if (valid && changes) answer++;
    }
    return answer;
};