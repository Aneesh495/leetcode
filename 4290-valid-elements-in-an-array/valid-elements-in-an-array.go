func findValidElements(nums []int) []int {
    rightRecord := make([]bool,len(nums))
    largest := 0
    for i := len(nums)-1; i >= 0; i-- {
        if nums[i] > largest { rightRecord[i],largest = true,nums[i] }
    }
    result := make([]int,0,len(nums))
    largest = 0
    for i, value := range nums {
        if value > largest || rightRecord[i] { result = append(result,value) }
        if value > largest { largest = value }
    }
    return result
}