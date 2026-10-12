a = [450, 520, 610, 720, 850, 920, 35, 80, 120, 200, 310]
left=0
right=len(a)-1
minimum=0
while left<=right:
    mid=(left+right)//2
    if mid<minimum:
        minimum=a[mid]
    elif mid>minimum:
        right=mid-1
        minimum=a[right]
    else:
        left=mid+1
        minimum=a[left]
print(minimum)
    