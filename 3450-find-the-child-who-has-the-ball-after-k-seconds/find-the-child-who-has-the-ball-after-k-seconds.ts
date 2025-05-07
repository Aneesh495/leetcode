function numberOfChild(n: number, k: number): number {
    const period = 2 * (n - 1);
    const position = k % period;
    return position < n ? position : period - position;
}