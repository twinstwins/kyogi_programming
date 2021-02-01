# 整数n個の要素からなる配列の入力
n,a,b = list(map(int,input().split()))
# 文字列を1文字ずつ分割して配列に格納 ex.abc => ['a','b','c']
arr = list(input())

cond = a + b
b_rank = 1

for man in arr:
    if man == 'a' and (cond > 0):
        print('Yes')
        cond -= 1
    elif man == 'b' and (cond > 0) and (b_rank <= b):
        print('Yes')
        b_rank += 1
        cond -= 1
    else:
        print('No')