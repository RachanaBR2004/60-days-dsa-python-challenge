a=[0,1,0,3,12]
left=0
for i in range(len(a)):
    if a[i]!=0:
        a[left],a[i]=a[i],a[left]
        left+=1
print(a)
    