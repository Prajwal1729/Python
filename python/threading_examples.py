from threading import Thread,Lock,current_thread
from queue import Queue
import time
db_val = 0
# def square_numbers():
#     for i in range(100):
#         i * i
    
    # threads = []
    # num_ths = 10

    # for i in range(num_ths):
    #     t = Thread(target=square_numbers)
    #     threads.append(t)


    # for t in threads:
    #     t.start()
    
    # for t in threads:
    #     t.join()

# def increase(lock):
#     global db_val
#     # lock.acquire()
#     with lock:
#         local_copy = db_val
#     # processing
#         local_copy +=1
#         time.sleep(0.1)
#         db_val = local_copy

def worker(q,lock):
    while True:
        val = q.get()
        # processing.....
        with lock:
          print(f"in {current_thread().name} got {val}")
        q.task_done()


if __name__ == "__main__":

    # lock = Lock()
    # print("start value",db_val)
    # t1 = Thread(target=increase,args=(lock,))
    # t2 = Thread(target=increase,args=(lock,))

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    # print("end value",db_val)

    q = Queue()
    # q.put(1)
    # q.put(2)
    # q.put(3)
    # q.put(4)

    # f1 = q.get()
    # print(f1)

    # q.task_done()
    # q.join()

    num_ths = 10
    lock = Lock()
    for i in range(num_ths):
        t = Thread(target=worker,args=(q,lock))
        t.daemon = True
        t.start()
    
    for i in range(1,21):
        q.put(i)

    q.join()        

    print("End main")