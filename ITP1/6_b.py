# n = int(input())
# mark,num = input().split()
# num = int(num)

n = 2
mark,num = ["H", 13]

cards = [[False for i in range(13)] for j in range(4)]

pattern = ["S", "H", "C", "D"]

for i in range(n):
    mark,num=input().split()
    num = int(num)
    cards[pattern.index(mark)][num-1] = True

for i in range(4):
    for j in range(13):
        if not cards[i][j]:
            print("{} {}".format(pattern[i],j+1))



n = int(input())

# 4種類*14枚のカードを表す二次元配列を作成
# リスト内包表記によるリスト作成 デフォルト値を設定して、range()で指定した個数の配列要素が追加
cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]

for i in range(n):
    mark,num=input().split()
    num = int(num)
    cards[pattern.index(mark)][num-1] = True

for i in range(4):
    for j in range(13):
        if not cards[i][j]:
            print(pattern[i],j+1)