s=str('-')
s1=str('.|.')
m,n=map(int,raw_input().split())
for i in range(1,m,2):
    print ((s1)*i).center(n,s)
print str('WELCOME').center(n,s)
for i in range(m-2,0,-2):
    print ((s1)*i).center(n,s)


