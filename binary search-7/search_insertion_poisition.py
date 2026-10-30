a=[10,20,30,40,50,60]
target=61

left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        print("found")
        break
    elif a[mid]<target:
        left=mid+1
    else:
        right=mid-1
else:
    print(left)