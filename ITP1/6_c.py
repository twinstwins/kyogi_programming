n = int(input())
arr = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

for t in range(n):
    b,f,r,v = map(int,input().split())
    arr[b-1][f-1][r-1] += v

for i in range(4):
    if i != 0:
        print("#"*20)
    for j in range(3):
        print(*[""]+arr[i][j])