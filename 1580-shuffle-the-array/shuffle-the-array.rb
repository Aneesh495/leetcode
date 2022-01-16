# @param {Integer[]} nums
# @param {Integer} n
# @return {Integer[]}
def shuffle(nums, n)
  result = Array.new(2 * n)
  n.times do |i|
    result[2 * i] = nums[i]
    result[2 * i + 1] = nums[i + n]
  end
  result
end