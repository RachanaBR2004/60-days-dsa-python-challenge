a=[10,20,30,40,50,60,70]
target=50
left=0
right=len(a)-1
mid=(left+right)//2
flag=False

while left<=right:
    mid=(left+right)//2
    if a[mid]==target:
        flag=True
        break
    elif a[mid]>target:
        right=mid-1
    else:
        left=mid+1
if flag==True:
    print("found")
else:
    print("not found")



