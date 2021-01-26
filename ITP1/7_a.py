
while True:
    m,f,r = map(int,input().split())

    if m == -1 & r ==-1 & f==-1:
        break

    sum = m + f
    if (m == -1 or f == -1):
        print("F")
        continue
    if sum < 30:
        print("F")
        continue
    if sum >= 80:
        print("A")
        continue
    if sum >= 65 and sum < 80:
        print("B")
        continue
    if (sum >= 50 and sum < 65) or r >= 50:
        print("C")
        continue
    if sum >= 30 and sum < 50:
        print("D")
        continue
