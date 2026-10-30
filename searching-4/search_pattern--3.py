a=[1,2,3,4,5,6,7]
num=int(input("enter the search num:"))
found=False
for i in a:
    if num==i:
        found=True
if found==True:
    print("found")
else:
    print("not found")


