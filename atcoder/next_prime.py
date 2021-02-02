x = int(input())

while True:

    cnt = 0

# xが素数であるならば、xは1とその数自身(x)でしか割り切れない
# 2からx-1までの数で割ってみて、割り切れるのであれば素数ではない

    for i in range(2,x):
        if x % i ==  0:
            cnt += 1
    if cnt == 0:
         print(x)
         break
    else:
        x += 1