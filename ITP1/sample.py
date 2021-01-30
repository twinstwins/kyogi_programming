# n = 2
# arr = [1,4]
# ans_arr = []

# n = 7
# arr = [14,14,2,13,56,2,37]
# ans_arr = []

n = int(input())
arr = list(map(int,input().split()))
ans_arr = []

for i in range(1,101):
    temp = 0
    for x in arr:
        temp += ((x - i)**2)
    ans_arr.append(temp)

print(min(ans_arr))