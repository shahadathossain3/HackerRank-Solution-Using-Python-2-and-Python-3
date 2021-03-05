import datetime
m,d,y=map(int,raw_input().split())
mydate = datetime.date(y,m,d)
x=mydate.strftime("%A")
print(x.upper())