n = int(input())
arr = input().split()

# n = 3
# arr = ["1","2","3"]

cnt = 0
ans_arr = []
while cnt < n:
    ans = arr.pop(-1)
    ans_arr.append(ans)
    cnt += 1

print(' '.join(ans_arr))