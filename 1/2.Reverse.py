entry=input("Enter: ")
try:
    num=int(entry)
    length=len(str(num))
    rev=[]
    x=0
    while length>=1:
        x=x+((num%10)*(10**(length-1)))
        num=num//10
        length-=1
    print(x)
except ValueError:
    length=len(entry)
    mylist=[]
    i=0
    while i<= length-1:
        mylist.append(entry[i])
        i+=1
    reverseList = mylist[::-1]
    rev_word = ""
    for n in reverseList:
        rev_word = rev_word + n
    print("Reverse Word is :"+rev_word)