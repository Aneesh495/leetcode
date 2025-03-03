def result_array(nums)
  values = nums.uniq.sort
  rank = {}
  values.each_with_index { |value, i| rank[value] = i + 1 }
  bit1 = Array.new(values.length + 1, 0)
  bit2 = Array.new(values.length + 1, 0)

  add = lambda do |tree, index|
    while index < tree.length
      tree[index] += 1
      index += (index & -index)
    end
  end
  prefix = lambda do |tree, index|
    total = 0
    while index > 0
      total += tree[index]
      index -= (index & -index)
    end
    total
  end

  first = [nums[0]]
  second = [nums[1]]
  add.call(bit1, rank[nums[0]])
  add.call(bit2, rank[nums[1]])
  nums.drop(2).each do |value|
    r = rank[value]
    greater1 = first.length - prefix.call(bit1, r)
    greater2 = second.length - prefix.call(bit2, r)
    if greater1 > greater2 || (greater1 == greater2 && first.length <= second.length)
      first << value
      add.call(bit1, r)
    else
      second << value
      add.call(bit2, r)
    end
  end
  first + second
end