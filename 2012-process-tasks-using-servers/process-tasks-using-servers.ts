class TaskHeap<T> {
    private data: T[] = [];
    constructor(private compare: (a: T, b: T) => number) {}
    size(): number { return this.data.length; }
    peek(): T | undefined { return this.data[0]; }
    push(value: T): void {
        this.data.push(value);
        let i = this.data.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (this.compare(this.data[p], this.data[i]) <= 0) break;
            [this.data[p], this.data[i]] = [this.data[i], this.data[p]];
            i = p;
        }
    }
    pop(): T {
        const root = this.data[0];
        const last = this.data.pop()!;
        if (this.data.length > 0) {
            this.data[0] = last;
            let i = 0;
            while (true) {
                let smallest = i;
                const left = 2 * i + 1, right = left + 1;
                if (left < this.data.length && this.compare(this.data[left], this.data[smallest]) < 0) smallest = left;
                if (right < this.data.length && this.compare(this.data[right], this.data[smallest]) < 0) smallest = right;
                if (smallest === i) break;
                [this.data[i], this.data[smallest]] = [this.data[smallest], this.data[i]];
                i = smallest;
            }
        }
        return root;
    }
}

function assignTasks(servers: number[], tasks: number[]): number[] {
    const free = new TaskHeap<number>((a, b) => servers[a] - servers[b] || a - b);
    const busy = new TaskHeap<[number, number]>((a, b) => a[0] - b[0] || a[1] - b[1]);
    for (let i = 0; i < servers.length; i++) free.push(i);
    const answer = new Array<number>(tasks.length);
    let time = 0;
    for (let i = 0; i < tasks.length; i++) {
        time = Math.max(time, i);
        while (busy.size() > 0 && busy.peek()![0] <= time) free.push(busy.pop()[1]);
        if (free.size() === 0) {
            time = busy.peek()![0];
            while (busy.size() > 0 && busy.peek()![0] <= time) free.push(busy.pop()[1]);
        }
        const server = free.pop();
        answer[i] = server;
        busy.push([time + tasks[i], server]);
    }
    return answer;
}