# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def min_size_subarray(nums, target)
    total = nums.sum
    cycles, remainder = target.divmod(total)
    base_length = cycles * nums.length
    return base_length if remainder == 0

    left = 0
    sum = 0
    best = nums.length + 1
    (0...(2 * nums.length)).each do |right|
        sum += nums[right % nums.length]
        while left <= right && sum >= remainder
            if sum == remainder && left < nums.length
                best = [best, right - left + 1].min
            end
            sum -= nums[left % nums.length]
            left += 1
        end
    end
    best > nums.length ? -1 : base_length + best
end