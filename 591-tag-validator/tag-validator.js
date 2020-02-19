var isValid = function(code) {
    const stack = [];
    const validName = name => /^[A-Z]{1,9}$/.test(name);
    let i = 0;
    while (i < code.length) {
        if (stack.length === 0 && i !== 0) return false;
        if (code.startsWith('<![CDATA[', i)) {
            if (stack.length === 0) return false;
            const end = code.indexOf(']]>', i + 9);
            if (end === -1) return false;
            i = end + 3;
        } else if (code[i] === '<') {
            const end = code.indexOf('>', i);
            if (end === -1) return false;
            const token = code.slice(i + 1, end);
            if (token.startsWith('/')) {
                const name = token.slice(1);
                if (!validName(name) || stack.length === 0 || stack[stack.length - 1] !== name) return false;
                stack.pop();
                if (stack.length === 0 && end !== code.length - 1) return false;
            } else {
                if (!validName(token)) return false;
                stack.push(token);
            }
            i = end + 1;
        } else {
            if (stack.length === 0) return false;
            i++;
        }
    }
    return stack.length === 0;
};