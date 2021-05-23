from random import *
a=randint(0,2)
b=eval(input("计算机的数已经准备好。\n请猜猜这个数：\n"))
if (a==b):
    print("你猜中了！\n")
elif (a>b):
    print("你猜的数太小了。计算机的数是：", a)
elif (a<b):
    print("你猜的数太大了。计算机的数是：", a)
