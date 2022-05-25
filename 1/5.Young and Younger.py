age=input("Enter Age :")
try:
    int_age=int(age)
    if int_age<=0 :
        print("Koskholi ?!!! Age manfi ya sefr darim ?!")
    elif int_age<=18:
        print("you are too young")
    elif int_age==19:
        print("Hi Little AmirAli Nodehi")
    elif int_age>19 and int_age<60:
        print("Not too young but still young")
    else:
        print("Too Old for this SHIT")
except ValueError:
    print(" -____- ")