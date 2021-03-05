from itertools import permutations
s,n=raw_input().split()
p=s.upper()
b=sorted(p)
t=permutations(b,int(n))
for i in t:
    print ''.join(i)