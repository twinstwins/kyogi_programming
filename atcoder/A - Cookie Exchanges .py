a,b,c = list(map(int,input().split()))

cnt = 0
# いずれかが奇数の場合は、その時点で終了
if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
    print(0)
    exit()

# 全て同じ数の場合、分けて数字を変更しても延々と同じことを繰り返す ex. 2 2 2 -> 2 2 2
if a == b == c:
    print(-1)
    exit()

while a % 2 == b % 2 == c % 2 ==0:
    a, b, c = (b+c) / 2, (a+c) / 2, (a+b) / 2
    cnt += 1

print(cnt)