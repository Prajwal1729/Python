# collection: Counter,namedtuple,OrderedDict,defaultdict,deque

import collections
from collections import Counter

a = "aaasjdjjbdowiwjoi"
my_count = Counter(a)
print(my_count)
print(my_count.values())
print(my_count.most_common(1))
print(list(my_count.elements()))

from collections import namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1,-2)
print(pt)
print(pt.x,pt.y)

from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print(ordered_dict)

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['c'])

from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.append(4)

print(d)
print(d.pop())

d.appendleft(34)
d.appendleft(89)
d.appendleft(100)
d.appendleft(134)
print(d)

d.extendleft([100,200,300])
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)







