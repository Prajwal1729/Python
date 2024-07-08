# with open('code.txt','w') as file:
#     file.write('Some todo...')

# file = open('code.txt','w')
# try:
#     file.write("Some to do..")
# finally:
#     file.close()


# from threading import Lock

# lock = Lock()
# lock.acquire()
# lock.release()


# class ManagedFile:
#     def __init__(self,filename):
#         self.filename = filename
    
#     def __enter__(self):
#         print('enter')
#         self.file = open(self.filename,'w')
#         return self.file

#     def __exit__(self,exc_type,exc_value,exc_traceback):
#         if self.file:
#             self.file.close()
#         if exc_type is not None:
#             print('exception has been handled')
#         print('exc:',exc_type,exc_value)
#         print('exit')
#         return True

# with ManagedFile('code.txt') as file:
#     print("do some stuff")
#     file.write('some Text...')
#     file.somemethod()
# print("Continuing")

# from contextlib import contextmanager

# @contextmanager
# def open_manage_file(filename):
#     f = open(filename,'w')
#     try:
#         yield f
#     finally:
#         f.close()

# with open_manage_file('notes.txt') as f:
#     f.write("will to something")
    







