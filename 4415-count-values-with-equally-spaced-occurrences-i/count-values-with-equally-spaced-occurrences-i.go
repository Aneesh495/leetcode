func countSpecialIntegers(nums []int) int {
    var locations [101][]int
    for index, value := range nums { locations[value] = append(locations[value], index) }
    result := 0
    for _, positions := range locations {
        // A special value has exactly three occurrences and two identical gaps.
        if len(positions) == 3 && positions[1]-positions[0] == positions[2]-positions[1] {
            result++
        }
    }
    return result
}