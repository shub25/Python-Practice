# from threading import Thread
# import time

# def print_zero():
#    for _ in range(5):
#        print(0)
#        time.sleep(1)    

# def print_odd():
#     cnt=1
#     for _ in range(5):
#         print(cnt)
#         cnt+=2
#         time.sleep(1)


# def print_even():
#     cnt=2
#     for _ in range(5):
#         print(cnt)
#         cnt+=2
#         time.sleep(2)

# if __name__=="__main__":
    
#     t1=Thread(target=print_zero)
#     t2=Thread(target=print_odd)
#     t3=Thread(target=print_even)

#     t1.start()
#     t2.start()
#     t3.start()

#     t1.join()
#     t2.join()
#     t3.join()

# import logging
# # import threading
# import time
# import concurrent.futures

# def thread_function(name):
#     logging.info("Thread %s: starting", name)
#     time.sleep(2)
#     logging.info("Thread %s: finishing", name)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()

#     for index, thread in enumerate(threads):
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")

#     with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
#         executor.map(thread_function, range(3))



from threading import Thread, Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.num = 1
        self.turn = 'zero'  # zero -> odd -> zero -> even -> ...
        self.cv = Condition()

    def print_zero(self):
        for _ in range(self.n):
            with self.cv:
                while self.turn != 'zero':
                    self.cv.wait()
                print(0, end='')
                self.turn = 'odd' if self.num % 2 == 1 else 'even'
                self.cv.notify_all()

    def print_odd(self):
        for _ in range((self.n+1)//2):
            with self.cv:
                while self.turn != 'odd':
                    self.cv.wait()
                if self.num % 2 == 1:
                    print(self.num, end='')
                    self.num += 1
                    self.turn = 'zero'
                    self.cv.notify_all()

    def print_even(self):
        for _ in range((self.n)//2):
            with self.cv:
                while self.turn != 'even':
                    self.cv.wait()
                if self.num % 2 == 0:
                    print(self.num, end='')
                    self.num += 1
                    self.turn = 'zero'
                    self.cv.notify_all()


if __name__ == "__main__":
    n = 1000000 # Set how far you want to go
    zeo = ZeroEvenOdd(n)

    t1 = Thread(target=zeo.print_zero)
    t2 = Thread(target=zeo.print_odd)
    t3 = Thread(target=zeo.print_even)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
