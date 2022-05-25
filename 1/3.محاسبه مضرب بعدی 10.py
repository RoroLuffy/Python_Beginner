num=input("Enter The Number:")
try:
    int_num=int(num)
    if int_num%10==0:
        print(int_num+10)
    elif int_num%10!=0:
        baghi=10-int_num%10
        print(int_num+baghi)
      #  print("The Number is Not Mazrab 10")
except ValueError:
    print("What The Fuck Are You Doing , Nigga")