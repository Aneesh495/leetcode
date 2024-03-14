# @param {Integer[]} nums
# @return {Integer}
def sum_of_power(nums)
  mod = 1_000_000_007
  nums.sort!
  prefix_min_sums = 0
  answer = 0
  nums.each do |x|
    answer = (answer + x * x * (prefix_min_sums + x)) % mod
    prefix_min_sums = (2 * prefix_min_sums + x) % mod
  end
  answer
end