func smallerNumbersThanCurrent(nums []int) []int {
    frequency := [101]int{}
    for _, value := range nums { frequency[value]++ }
    count := 0
    for value, occurrences := range frequency {
        // Record the number strictly smaller before adding the current bucket.
        frequency[value] = count
        count += occurrences
    }
    answer := make([]int, len(nums))
    for i, value := range nums { answer[i] = frequency[value] }
    return answer
}