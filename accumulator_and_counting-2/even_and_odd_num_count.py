
# count even num

a=[1,2,3,45,6,7,8,90]
count=0
for i in a:
    if i%2==0:
        count=count+1
print("even num is:",count)


# count positiv num
a=list(map(int,input("enter array:").split()))
count=0
for i in a:
    if i>=0:
        count=count+1
print("positive num:",count)

#count even and odd num 

a=list(map(int,input("enter array:").split()))
ecount=0
ocount=0
for i in a:
    if i%2==0:
        ecount=ecount+1
    else:
        ocount=ocount+1
print("even:",ecount)
print("odd:",ocount)