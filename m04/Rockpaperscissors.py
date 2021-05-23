from random import *
a=randint(0,2)
b=eval(input("0 代表石头，1 代表剪刀，2 代表布。请选择：\n"))
if (a==b):
    print("平局！\n")
elif (a == 0):
    if (b == 1):
        print("你输了。计算机出的是石头。\n石头战胜剪刀。")
    else:
        print("你赢了。计算机出的是石头。\n布战胜石头。")
elif (a == 1):
    if (b == 0):
        print("你赢了。计算机出的是剪刀。\n石头战胜剪刀。")
    else:
        print("你输了。计算机出的是剪刀。\n剪刀战胜布。")
else:
    if (b == 0):
        print("你输了。计算机出的是布。\n布战胜石头。")
    else:
        print("你赢了。计算机出的是布。\n剪刀战胜布。")

