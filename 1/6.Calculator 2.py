formul=input("Enter The Value: ")
for i in formul:
    if i=="+":
        for i in formul:
         num=formul.split("+")
        print(int(num[0])+int(num[1]))
    elif i=="-":
        for i in formul:
         num=formul.split("-")
        print(int(num[0])-int(num[1]))
    elif i=="*":
        for i in formul:
         num=formul.split("*")
        print(int(num[0])*int(num[1]))
    elif i=="/":
        for i in formul:
         num=formul.split("/")
        print(int(num[0])/int(num[1]))