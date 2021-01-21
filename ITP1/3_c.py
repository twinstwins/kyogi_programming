a,b,c=map(int,input().split())
# a,b,c=[5,14,80]// => 3
ans=0
for i in range (a,b+1):
    if c%i==0:
        ans+=1
print(ans)