a,b = map(int,input().split())
# a,b = [3,2]
a,b = map(int,input().split())
d = a // b
r = a % b
f = a / b

print(d,r,'{:.5f}'.format(f))
