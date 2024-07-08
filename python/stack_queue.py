
# implementation of stack(LIFO)

import collections
stack = collections.deque()
stack.append(12)
stack.append(14)
stack.append(190)
stack.append(140)
print(stack)
print(stack.pop())


import queue
stack = queue.LifoQueue(4)
stack.put(12)
stack.put(13)
stack.put(14)
stack.put(15)
print(stack)
print(stack.get())


# Implementation of Queue(FIFO)

import collections
queue = collections.deque()
queue.appendleft(34)
queue.appendleft(90)
queue.appendleft(100)
queue.appendleft(200)
print(queue)
print(queue.pop())

import queue
queue = queue.Queue(4)
queue.put(90)
queue.put(100)
queue.put(110)
queue.put(120)
print(queue)
print(queue.get())