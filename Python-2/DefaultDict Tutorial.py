from collections import defaultdict
d=defaultdict(list)
n,m=map(int,raw_input().split())
for i in range (0,n):
    d[raw_input()].append(i+1)
for i in range(0,m):
    s=raw_input()
    if s in d:
        print " ".join(map(str,d[s]))
    else:
        print "-1"