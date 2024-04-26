class Solution {
    func distanceTraveled(_ mainTank: Int, _ additionalTank: Int) -> Int {
        let transfers = min(additionalTank, (mainTank - 1) / 4)
        return (mainTank + transfers) * 10
    }
}