import string
    
def print_rangoli(size):
    mid = size-1
    for i in range(1,size):
        row=['-']*(2*size-1)
        for j in range(0,i):
            row[mid-j] = row[mid+j]=string.ascii_lowercase[size-i+j]
        print  '-'.join(row)
    for i in range (0,size):
        row=['-']*(2*n-1)
        for j in range(0,n-i):
            row[mid-j]=row[mid+j]=string.ascii_lowercase[i+j]
        print  '-'.join(row)

