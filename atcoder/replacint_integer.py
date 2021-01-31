n,k = list(map(int,input().split()))
t = n % k
arr = [t,abs(k-t)]

print(min(arr))