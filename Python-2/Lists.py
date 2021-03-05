n = int(raw_input())
lst = []
for _ in range(n):
    inpt = raw_input().split()
    if inpt[0] == 'insert':
        lst.insert(int(inpt[1]),int(inpt[2]))
    elif inpt[0]=='print':
        print lst
    elif inpt[0]=='remove':
        lst.remove(int(inpt[1]))
    elif inpt[0]=='append':
        lst.append(int(inpt[1]))
    elif inpt[0]=='sort':
        lst.sort()
    elif inpt[0]=='print':
        print lst
    elif inpt[0]=='pop':
        lst.pop()
    elif inpt[0]=='reverse':
        lst.reverse()
    elif inpt[0]=='print':
        print lst