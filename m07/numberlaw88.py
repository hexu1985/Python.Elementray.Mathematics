number1=0
number2=7
value=0
for i in range(8):
    number1=10*number1+(9-i)
    value=number1*9+number2
    print("%s%d X 9 + %d = %d" % ((8-i)*" ", number1, number2, value))
    number2-=1

