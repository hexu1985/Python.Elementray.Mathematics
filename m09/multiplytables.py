print("九九乘法表")
print('--------------------------------------------------')
for i in range(1,10):
    for j in range(1,10):
        if i*j<10:
            print('%d * %d = %d' % (i, j, i*j), end=2*' ')
        else:
            print('%d * %d = %d' % (i, j, i*j), end=' ')
    print(' ')
