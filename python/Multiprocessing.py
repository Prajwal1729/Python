import multiprocessing
import multiprocessing.process
import requests

def downloadFile(url,name):
    print(f"Start downloading file{name}")
    response = requests.get(url)
    open(f"file1/{name}.jpg","wb").write(response.content)
    print(f"Finished downloading file{name}")
    

url = "http://picsum.photos/2000/3000"
pros = []

for i in range(15):
    # downloadFile(url,i)    
    p = multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()


from multiprocessing import Process
import os
import time

def square_nums():
    for i in range(100):
        i*i
        time.sleep(0.1)


threads = []
num_ths = 10
ps = []
num_ps = os.cpu_count()

# Processing:

for i in range(num_ps):                 # type: ignore
    p = Process(target=square_nums)
    ps.append(p)


for p in ps:
    p.start()

for p in ps:
    p.join()

print("end main")


# Threading:
from threading import Thread
for i in range(num_ths):
    t = Thread(target=square_nums)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:    
    t.join()

print("end main")




    

