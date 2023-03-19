# @param {Integer[]} digits
# @return {Integer[]}
def find_even_numbers(digits)
    count = Array.new(10, 0)
    digits.each { |d| count[d] += 1 }
    result = []

    (1..9).each do |hundreds|
        next if count[hundreds] == 0
        count[hundreds] -= 1
        (0..9).each do |tens|
            next if count[tens] == 0
            count[tens] -= 1
            (0..8).step(2) do |ones|
                result << hundreds * 100 + tens * 10 + ones if count[ones] > 0
            end
            count[tens] += 1
        end
        count[hundreds] += 1
    end
    result
end