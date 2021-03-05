n=int(raw_input())
for _ in range (n):
    try:
        a,b=map(int,raw_input().split())
        print a/b
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as e:
        print "Error Code:",e