type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
    return function(...args: any[]) {
        return new Promise<any>((resolve, reject) => {
            const timer = setTimeout(() => reject("Time Limit Exceeded"), t);
            Promise.resolve()
                .then(() => fn(...args))
                .then(
                    value => { clearTimeout(timer); resolve(value); },
                    error => { clearTimeout(timer); reject(error); }
                );
        });
    };
};