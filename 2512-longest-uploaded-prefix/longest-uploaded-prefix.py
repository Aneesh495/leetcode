class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = bytearray(n + 2)
        self.end = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = 1
        # The frontier moves at most n times over all uploads combined.
        while self.uploaded[self.end + 1]:
            self.end += 1

    def longest(self) -> int:
        return self.end