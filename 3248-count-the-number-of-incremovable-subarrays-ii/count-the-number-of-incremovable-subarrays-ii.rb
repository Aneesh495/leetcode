# @param {Integer[]} nums
# @return {Integer}
def incremovable_subarray_count(nums)
  n = nums.length
  prefix_len = 1
  while prefix_len < n && nums[prefix_len - 1] < nums[prefix_len]
    prefix_len += 1
  end
  return n * (n + 1) / 2 if prefix_len == n

  suffix_start = n - 1
  while suffix_start > 0 && nums[suffix_start - 1] < nums[suffix_start]
    suffix_start -= 1
  end

  answer = 0
  j = suffix_start
  (0..prefix_len).each do |i|
    j = [j, i + 1].max
    while j < n && i > 0 && nums[i - 1] >= nums[j]
      j += 1
    end
    answer += n - j + 1
  end
  answer
end