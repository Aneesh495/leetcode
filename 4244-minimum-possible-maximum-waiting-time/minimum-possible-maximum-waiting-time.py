class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        states = {(fuel[0], fuel[1], 0, 0): 0}
        for index, need in enumerate(demand):
            following = {}
            for (fuel0, fuel1, busy0, busy1), worst in states.items():
                # Busy times are measured relative to the current car's allowed start.
                if fuel0 >= need:
                    key = (fuel0 - need, fuel1, need, max(0, busy1 - busy0))
                    new_worst = max(worst, busy0)
                    following[key] = min(new_worst, following.get(key, new_worst))
                if fuel1 >= need:
                    key = (fuel0, fuel1 - need, max(0, busy0 - busy1), need)
                    new_worst = max(worst, busy1)
                    following[key] = min(new_worst, following.get(key, new_worst))
            if not following:
                return min(states.values()) if index else -1
            states = following
        return min(states.values())