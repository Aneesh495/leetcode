# @param {String[]} words
# @return {Integer[]}
def sum_prefix_scores(words)
    children = {}
    counts = [0]
    words.each do |word|
        node = 0
        word.each_byte do |byte|
            key = node * 26 + byte - 97
            child = children[key]
            unless child
                child = counts.length
                children[key] = child
                counts << 0
            end
            node = child
            counts[node] += 1
        end
    end

    words.map do |word|
        node = 0
        score = 0
        word.each_byte do |byte|
            node = children[node * 26 + byte - 97]
            score += counts[node]
        end
        score
    end
end