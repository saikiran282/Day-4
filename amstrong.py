# amstrong
n=int(input())
l=len(str(n))
su=0
for i in str(n):
    su+=int(i)**l
if int(su)==n:
    print("amstron")
else:
     print("not amstron")
    
