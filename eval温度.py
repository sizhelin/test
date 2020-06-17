FUHAO = input("输入温度符号：")
WENDU = eval(input("请输入温度的数值："))

if FUHAO in ['F','f']:
	C = int ((WENDU-32)/1.8)
	print("转换后的温度是",C,"C")
elif FUHAO in ['C','c']:
	F = int (1.8*WENDU+32)
	print("转换后的温度是",F,"F")
else:
	print("输入格式错误")
