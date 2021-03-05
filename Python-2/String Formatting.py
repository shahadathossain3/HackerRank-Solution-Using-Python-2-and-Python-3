def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range (1,number+1):
        print  str(i).rjust(width," "),oct(i)[1:].rjust(width," "),hex(i)[2:].rjust(width," ").upper(), bin(i)[2:].rjust(width," ")

