function countTriplets(arr: number[]): number {
    let prefixXor = 0;
    let answer = 0;
    const stats = new Map<number, [number, number]>();
    stats.set(0, [1, 0]);

    for (let end = 1; end <= arr.length; end++) {
        prefixXor ^= arr[end - 1];
        const [count, sumIndices] = stats.get(prefixXor) ?? [0, 0];
        answer += count * (end - 1) - sumIndices;
        stats.set(prefixXor, [count + 1, sumIndices + end]);
    }
    return answer;
}