w,h,x,y,r = map(int,input().split())

w,h,x,y,r = [5,4,2,2,1]
if (x-r < 0 or x+r > w) or (y-r < 0 or y+r > h) :
    print('No')
else:
    print('Yes')