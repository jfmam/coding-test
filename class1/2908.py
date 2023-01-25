from functools import reduce
n,m = input().split()
a = reversed(list(n))
b = reversed(list(m))
c = int(reduce(lambda x,y: x+y, a))
d = int(reduce(lambda x, y: x+y, b))

print(max(c,d))
