from itertools import product
a=map(int,raw_input().split())
b=map(int,raw_input().split())
a.sort()
b.sort()
#c=list(product(a,b))
print ' '.join(str(i) for i in (product(a,b)))