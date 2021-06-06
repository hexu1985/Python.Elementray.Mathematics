number=0
for i in range(9):
    number=10*number+1
    print("%s%d X %d%s = %d" % ((9-i)*" ", number, number, (9-i)*" ", number*number))
