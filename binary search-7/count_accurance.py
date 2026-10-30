
# count taget accurance
a = [1, 2, 2, 2,2,2, 3, 4,4,4,5]
target = 5
left=0
right=len(a)-1
first=-1
# search left side
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        first=mid
        right=mid-1
    elif a[mid]>target:
        right=mid-1
    else:
        left=mid+1

# search right side
left=0
right=len(a)-1
last=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        last=mid
        left=mid+1
    elif a[mid]>target:
        right=mid-1
    else:
        left=mid+1

if first!=-1:
    count=last-first+1
    print("accurance",count)
else:
    print("not found")




