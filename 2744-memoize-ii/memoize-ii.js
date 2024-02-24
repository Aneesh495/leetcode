function memoize(fn) {
    const root = { next: new Map(), cached: false, value: undefined };
    return function(...args) {
        let node = root;
        // Each argument is one edge, so objects and functions retain their identity.
        for (const arg of args) {
            if (!node.next.has(arg)) {
                node.next.set(arg, { next: new Map(), cached: false, value: undefined });
            }
            node = node.next.get(arg);
        }
        if (!node.cached) {
            node.value = Reflect.apply(fn, this, args);
            node.cached = true;
        }
        return node.value;
    };
}