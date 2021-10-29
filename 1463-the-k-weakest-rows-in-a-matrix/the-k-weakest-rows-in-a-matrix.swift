class Solution {
    func kWeakestRows(_ mat: [[Int]], _ k: Int) -> [Int] {
        var counts = mat.enumerated().map { (index: $0.offset, soldiers: $0.element.reduce(0, +)) }
        counts.sort {
            if $0.soldiers == $1.soldiers { return $0.index < $1.index }
            return $0.soldiers < $1.soldiers
        }
        return counts.prefix(k).map { $0.index }
    }
}