import threading
import random
import time
import queue

q = queue.Queue(1000)


class DiningPhilosophers:
   def __init__(self, num=1):
       self.locks = [threading.Lock() for _ in range(5)]
       self.orders = [sorted([i, (i+1) % 5]) for i in range(5)]
       self.num = num

   def wantsToEat(self,
                  philosopher,
                  pickLeftFork,
                  pickRightFork,
                  eat,
                  putLeftFork,
                  putRightFork):

       for _ in range(self.num):
           with self.locks[self.orders[philosopher][0]]:
               with self.locks[self.orders[philosopher][1]]:
                   pickLeftFork(philosopher)
                   pickRightFork(philosopher)
                   eat(philosopher)
                   putLeftFork(philosopher)
                   putRightFork(philosopher)


def pickLeftFork(i):
    q.put([i, 1, 1])


def pickRightFork(i):
    q.put([i, 2, 1])


def eat(i):
    time.sleep(random.uniform(0.1, 1.0))
    q.put([i, 0, 3])


def putLeftFork(i):
    q.put([i, 1, 2])


def putRightFork(i):
    q.put([i, 2, 2])


if __name__ == "__main__":
    num = input('>>>')
    p1 = DiningPhilosophers(int(num))
    threads = []
    for i in range(5):
        t1 = threading.Thread(target=p1.wantsToEat, args=[i, pickLeftFork,
                                                          pickRightFork, eat, putLeftFork, putRightFork])
        threads.append(t1)

    for tr in threads:
        tr.start()

    for tr in threads:
        tr.join()

    items = []
    while True:
        items.append(q.get())
        if q.empty():
            break

    print(items)
