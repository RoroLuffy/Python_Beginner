count=0
for j in range(1,21):
    for i in range(1,21):
        if j%i==0:
            count+=1
    if count==2:
        print(j)
    count=0        