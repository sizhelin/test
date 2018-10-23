x=input("请输入一个整数判断是否为素数：")
x=int (x)
for i in range(2,x):
    if x % i == 0:
        print ("不是")
        break
else:
    print ("是")
