a = [450, 520, 610, 720, 850, 920, 35, 80, 120, 200, 310]
target = 452
left=0
right=len(a)-1
flag=False
index=-1

while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        flag=True
        index=mid
        break
    elif a[left]<=a[mid]:
        if a[left]<=target<a[mid]:
            right=mid-1
        else:
            left=mid+1
    else:
        if a[mid]<target<=a[right]:
            left=mid+1
        else:
            right=mid+1
if flag==True:
    print("index",index)
else:
    print(" not found")


