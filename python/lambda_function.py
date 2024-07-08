
# add100 = lambda x: x+100
# print(add100(6775))

# mult = lambda x,y : x*y
# print(mult(45,67))


l = [(1,2),(4,5),(9,10),(11,12)]

def sort_by(x):
    return x[l]
l_sort = sorted(l,key=lambda x: x[1])
print(l)
print(l_sort)


a = [1,2,3,4,5,67]
# product = filter(a, lambda y: y%2)
# res = filter(lambdo)

c = [x for x in a if x%2==0]
print(c)

from functools import reduce
prod_a = reduce(lambda x,y: x*y,a)
print(prod_a)





