#prime
n=int(input())
num=''
for i in range(1,n+1):
    s=0
    for k in range(2,n+1):
        if i%k==0:
            s+=1   
    if s==1:
        print(i,"prime")
        num=num+' '+str(i)
print(num)
        
        
