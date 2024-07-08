from multiprocessing import Process,Value,Array,Lock
from multiprocessing import Queue
from multiprocessing import Pool
import time

# def add_100(numbers,lock):
#     for i in range(numbers):
#         time.sleep(0.01)
#         # with lock:
#         # # lock.acquire()
#         #   number.value+=1
#         # # lock.release()
#         for n in numbers:
#             n+=1
#         for i in range(len(numbers)):
#             with lock:
#               numbers[i]+=1
            
# def sqaure_nums():
#     for i in range(100):
#         i*i
def sqaure(numbers,queue):
    for i in numbers:
        queue.put(i*i)

def make_neg(numbers,queue):
    for i in numbers:
        queue.put(-1*i)

def cube(num):
    return num*num*num

if __name__ == "__main__":
    # lock = Lock()
    # # shared_num = Value('i',0)
    # shared_arr = Array('d',[0.0,100.0,200.0])
    # print("Array at Beginning is:",shared_arr[:])

    # p1 = Process(target=add_100,args=(shared_arr,lock))
    # p2 = Process(target=add_100,args=(shared_arr,lock))


    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    # numbers = range(1,6)
    # q = Queue()
    # p1 = Process(target=sqaure,args=(numbers,q))
    # p2 = Process(target=make_neg,args=(numbers,q))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # print("Array at end is:",shared_arr[:])

    # while not q.empty():
    #     print(q.get())

    # pool = Pool()

    # map,apply,join,close

    numbers = range(10)
    pool = Pool()
    res = pool.map(cube,numbers)
    # pool.apply(cube,numbers[0])
    pool.close()
    pool.join()
    print(res)



    

