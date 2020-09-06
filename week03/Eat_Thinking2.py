import threading
import random
import time
import queue

q = queue.Queue(1000)

# 五个哲学家0-4，五把叉子也将拥有一样的编号0-4。
# 假如0号哲学家旁边的两把叉子是0/1，1号旁边的是1/2，2号旁边的是2/3，3号旁边的是3/4， 4号旁边的是4/0
# 只要每个人都先拿起自己旁边小号的叉子，就可以避免每人拿一把的尴尬。从而有机会吃到。
# 由于4号的左手是大号叉子，右手是小号叉子，要让他左右互换


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
      #根据进食次数循环
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

# 为避免跑的太快大家按顺序吃，延长进食时间


def eat(i):
    time.sleep(random.uniform(0.1, 1.0))
    q.put([i, 0, 3])


def putLeftFork(i):
    q.put([i, 1, 2])


def putRightFork(i):
    q.put([i, 2, 2])


#使用者指定一个进食次数num
if __name__ == "__main__":
    
    num = input('>>>')
    p1 = DiningPhilosophers(int(num))

    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=p1.wantsToEat, args=[i, pickLeftFork,
                                                                    pickRightFork, eat, putLeftFork, putRightFork]))
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
