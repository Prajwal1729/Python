# file objects

with open('test.txt','r') as f:
# f = open('test.txt','r')
# print(f.name)
# print(f.mode)
# f.close()

    # for l in f:
    #   print(l,end=" ")

   # f_contents = f.read()
    # f_contents = f.readline()
    # print(f_contents,end=" ")

    # f_contents = f.readline()
    # print(f_contents)

    # f_contents = f.read(100)
    # print(f_contents,end=" ")

    # f_contents = f.read(100)
    # print(f_contents,end=" ")

    # f_contents = f.read(100)
    # print(f_contents,end=" ")
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents,end="*")

    f_contents = f.read(size_to_read)
    print(f_contents,end="*")

    f.seek(0)  # sets the position in the file

    f_contents = f.read(size_to_read)
    print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents,end="*")
    #     f_contents = f.read(size_to_read)

    print(f.tell())  # current position in the file
    # print(f.closed)


    # writing in the file

with open('test.txt','r') as rf:
    with open('test_copy.txt','w') as wf:
        for l in rf:
            wf.write(l)


with open('shiva.jpg','rb') as rf:
    with open('shiva_copy.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)

     





   


    


