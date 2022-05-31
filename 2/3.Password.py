entry=input("Enter The Password: ")
#countA=0
countDigit=0
countSign=0
count8=0
for i in entry:
    count8+=1
    if i=="%" or "$" or "#" or "@":
        countSign+=1
    if i.isdigit():
        countDigit+=1
if entry.isupper()==True:
    print("Fucked Up Pass")
if entry.islower()==True:
    print("Fucked Up Pass")
if count8<=8 :
    print("Fucked Up Pass")
if countSign<=1:
    print("Fucked Up Pass")
if countDigit<=1:
    print("Fucked Up Pass")
else:
    print("OK")