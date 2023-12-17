
from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        """
        LeetCode 517. Super Washing Machines
        Goal: Minimum number of simultaneous moves to equalize loads
        Key facts:
          • If total dresses not divisible by number of machines, return -1
          • Let avg be target load per machine
          • Traverse left to right and track prefix imbalance s:
                s = sum(machines[:i+1]) - (i+1)*avg
            s > 0 means left side has surplus that must flow right
            s < 0 means left side needs that much from right
          • At machine i, the minimum steps needed is constrained by:
                1) local send or receive at i: load = machines[i] - avg
                2) net flow passing through due to prefix imbalance: abs(s)
            The answer is the max over all i of max(abs(s), load)
        Time O(n) Space O(1)
        """
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1

        avg = total // n
        res = 0
        s = 0  # prefix imbalance after processing i

        for load in machines:
            # local surplus or deficit at this machine relative to target
            diff = load - avg
            s += diff
            # max of:
            #   • abs(s): flow that must cross this boundary
            #   • diff: local send amount if positive
            res = max(res, abs(s), diff)
        return res
