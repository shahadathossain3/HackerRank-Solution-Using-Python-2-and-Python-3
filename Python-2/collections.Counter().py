from collections import Counter
x=int(raw_input())
money=0
n=list(map(int,raw_input().split()))
n1=Counter(n)
cstmr=int(raw_input())
for _ in range (cstmr):
    size,prige=map(int,raw_input().split())
    if n1[size]>0:
        n1[size]-=1
        money+=prige
print money