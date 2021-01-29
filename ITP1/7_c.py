h,c = map(int,input().split())
mat = []
for i in range(h):
    list1 = list(map(int,input().split()))
    list1.append(sum(list1))
    mat.append(list1)

for i in mat:
    print(*i)
colsum = []
for i in range(c+1):
    sum4 = 0
    for j in range(h):
        sum4+= mat[j][i]
    colsum.append(sum4)
print(*colsum)