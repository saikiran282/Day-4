num=input()
num2=list(map(int, input().split()))
countp=0
countn=0
countb=0
for i in num2:
    if i>0:
        countp+=1
    elif i<0:
        countn+=1
    else:
        countb+=1
print(countp,countn,countb)

    


