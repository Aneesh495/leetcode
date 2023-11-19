class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        free_start = 0
        free_length = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                free_length += 1
            else:
                free_length = 0
            if free_length == size:
                free_start = i - size + 1
                for index in range(free_start, i + 1):
                    self.memory[index] = mID
                return free_start
        return -1

    def freeMemory(self, mID: int) -> int:
        freed = 0
        for index, value in enumerate(self.memory):
            if value == mID:
                self.memory[index] = 0
                freed += 1
        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)