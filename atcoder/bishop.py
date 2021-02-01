h,w = list(map(int,input().split()))
if min(h,w) == 1:
    print(1)
    exit()

n = h * w

# nが偶数の場合、(n+1) / 2 を切り捨てた値は、n / 2 と等しい
# 5 / 2 = 2.5　　　　11 / 2 = 5.5
# nが奇数の場合(3*3=9)
# 9 / 2 = 10.5
# (9+1) / 2 = 5
# print((n+1) / 2)

print(((n+1) // 2))