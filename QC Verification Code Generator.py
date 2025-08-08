num=input()
l=len(str(num))
ind=l-1
for i in range(l+1):
    if int(num[ind])==0:
        ind-=1    
print(num[ind::-1])
   
