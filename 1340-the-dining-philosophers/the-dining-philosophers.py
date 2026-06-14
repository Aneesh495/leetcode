from threading import Lock, Semaphore

class DiningPhilosophers:

    def __init__(self):
        self.forks = [Lock() for _ in range(5)]
        self.room = Semaphore(4)

    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        
        left = philosopher
        right = (philosopher + 1) % 5

        self.room.acquire()
        self.forks[left].acquire()
        self.forks[right].acquire()

        pickLeftFork()
        pickRightFork()
        eat()
        putRightFork()
        putLeftFork()

        self.forks[right].release()
        self.forks[left].release()
        self.room.release()
