sum=0
for i in range(1, 1001):
    if i%7 == 0:
        print(i)
        sum=sum+i
print("从1到1000所有能被7整除的数的和为：", sum)
