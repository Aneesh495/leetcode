class BookMyShow {
    private rowCount: number;
    private seatsPerRow: number;
    private size: number;
    private sumTree: number[];
    private maxTree: number[];

    constructor(n: number, m: number) {
        this.rowCount = n;
        this.seatsPerRow = m;
        this.size = 1;
        while (this.size < n) this.size *= 2;
        this.sumTree = Array(2 * this.size).fill(0);
        this.maxTree = Array(2 * this.size).fill(0);
        for (let row = 0; row < n; row++) {
            this.sumTree[this.size + row] = m;
            this.maxTree[this.size + row] = m;
        }
        for (let node = this.size - 1; node > 0; node--) {
            this.sumTree[node] = this.sumTree[node * 2] + this.sumTree[node * 2 + 1];
            this.maxTree[node] = Math.max(this.maxTree[node * 2], this.maxTree[node * 2 + 1]);
        }
    }

    private update(row: number, remaining: number): void {
        let node = this.size + row;
        this.sumTree[node] = remaining;
        this.maxTree[node] = remaining;
        node = Math.floor(node / 2);
        while (node > 0) {
            this.sumTree[node] = this.sumTree[node * 2] + this.sumTree[node * 2 + 1];
            this.maxTree[node] = Math.max(this.maxTree[node * 2], this.maxTree[node * 2 + 1]);
            node = Math.floor(node / 2);
        }
    }

    private findFirst(node: number, left: number, right: number, maxRow: number, need: number): number {
        if (left > maxRow || this.maxTree[node] < need) return -1;
        if (left === right) return left;
        const mid = Math.floor((left + right) / 2);
        const first = this.findFirst(node * 2, left, mid, maxRow, need);
        if (first !== -1) return first;
        return this.findFirst(node * 2 + 1, mid + 1, right, maxRow, need);
    }

    private prefixSum(maxRow: number): number {
        let left = this.size;
        let right = this.size + maxRow + 1;
        let total = 0;
        while (left < right) {
            if (left % 2 === 1) total += this.sumTree[left++];
            if (right % 2 === 1) total += this.sumTree[--right];
            left = Math.floor(left / 2);
            right = Math.floor(right / 2);
        }
        return total;
    }

    gather(k: number, maxRow: number): number[] {
        const row = this.findFirst(1, 0, this.size - 1, maxRow, k);
        if (row === -1) return [];
        const available = this.sumTree[this.size + row];
        this.update(row, available - k);
        return [row, this.seatsPerRow - available];
    }

    scatter(k: number, maxRow: number): boolean {
        if (this.prefixSum(maxRow) < k) return false;
        let remaining = k;
        while (remaining > 0) {
            const row = this.findFirst(1, 0, this.size - 1, maxRow, 1);
            const available = this.sumTree[this.size + row];
            const take = Math.min(available, remaining);
            this.update(row, available - take);
            remaining -= take;
        }
        return true;
    }
}