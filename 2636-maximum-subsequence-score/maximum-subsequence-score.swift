class Solution {
    func maxScore(_ nums1: [Int], _ nums2: [Int], _ k: Int) -> Int {
        let order = nums2.indices.sorted { nums2[$0] > nums2[$1] }
        var heap: [Int] = []
        var sum = 0
        var answer = 0

        func push(_ value: Int) {
            heap.append(value)
            var i = heap.count - 1
            while i > 0 {
                let parent = (i - 1) / 2
                if heap[parent] <= heap[i] { break }
                heap.swapAt(parent, i)
                i = parent
            }
        }

        func popMin() -> Int {
            let result = heap[0]
            let last = heap.removeLast()
            if !heap.isEmpty {
                heap[0] = last
                var i = 0
                while true {
                    let left = 2 * i + 1
                    let right = left + 1
                    var smallest = i
                    if left < heap.count && heap[left] < heap[smallest] { smallest = left }
                    if right < heap.count && heap[right] < heap[smallest] { smallest = right }
                    if smallest == i { break }
                    heap.swapAt(i, smallest)
                    i = smallest
                }
            }
            return result
        }

        for index in order {
            push(nums1[index])
            sum += nums1[index]
            if heap.count > k { sum -= popMin() }
            if heap.count == k {
                answer = max(answer, sum * nums2[index])
            }
        }
        return answer
    }
}