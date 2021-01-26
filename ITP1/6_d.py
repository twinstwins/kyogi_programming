n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr2 = []
for i in range(m):
    arr2.append(int(input()))

# サンプル
# n,m = [3,4]
# arr = [[1,2,0,1],[0,3,0,1],[4,1,1,0]]
# arr2 = [1,2,3,0]

for i in range(n):
    ans = 0
    for j in range(m):
        ans += arr[i][j] * arr2[j]
        # print(arr[i][j] * arr2[j])
    print(ans)
