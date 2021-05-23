a=eval(input("请输入第一个数:\n"))
b=eval(input("请输入第二个数:\n"))
c=eval(input("请输入第三个数:\n"))
if (a>=b):
    if (c>=a):
        print("最大的数是：", c)
    else:
        print("最大的数是：", a)
else:
    if (c>=b):
        print("最大的数是：", c)
    else:
        print("最大的数是：", b)
