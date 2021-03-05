dic={}
n = int(raw_input())
for _ in range(n):
    name,mathe,chemistry,physics = raw_input().split(' ')
    dic[name]=(float(mathe)+float(chemistry)+float(physics))/3

result = raw_input()
if result in dic:
    print ("%.2f"%dic[result])
    