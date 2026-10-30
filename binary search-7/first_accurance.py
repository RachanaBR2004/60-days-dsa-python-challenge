a = [1, 2, 2, 3, 4,5,5]
target = 5
left=0
right=len(a)-1
ans=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        ans=mid
        right=mid-1

    elif a[mid]>target:
        right=mid-1
    else:
        left=mid+1
if ans!=-1:
    print("first accurance",ans)
else:
    print("not found")



#last_accurance

a = [1,1,2, 2, 2, 3, 4, 5]
target = 1
left=0
right=len(a)-1
answer=-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        answer=mid
        left=mid+1
    elif a[mid]>target:
        right=mid-1
    else:
        left=mid+1
if answer!=-1:
    print("last accurance",answer)
else:
    print("not found")

