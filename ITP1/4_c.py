while True:
    arr = input().split()

    a = int(arr[0])
    op = arr[1]
    b = int(arr[2])

    if op == '?':
        break

    if op == '+':
        print("{}".format(a+b))
    elif op == '-':
        print("{}".format(a-b))
    elif op == '/':
        print("{}".format(a//b))
    else:
        print("{}".format(a*b))