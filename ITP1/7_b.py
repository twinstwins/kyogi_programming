
while True:
    n,x = map(int,input().split())


    n,x = [5,9]

    arr = [[i for i in range(n)]]


    if n == 0 & x ==0:
        break

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(arr[i+1] + arr[j+1] + arr[k+1])
