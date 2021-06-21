a,b = list(map(int,input().split()))
# a,b = [1,3]

for n in range(a,b+1):
    n *= n

print(n)