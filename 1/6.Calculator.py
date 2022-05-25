num1=input("Enter The Number1:")
sign=input("Enter The sign:")
num2=input("Enter The Number2:")
int_num1=int(num1)
int_num2=int(num2)
if sign=="+":
    print(int_num1+int_num2)
elif sign=="-":
    print(int_num1-int_num2)
elif sign=="*":
    print(int_num1*int_num2)
elif sign=="/":
    print(int_num1/int_num2)
else:
    print("WTF")