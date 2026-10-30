# count positive num
a=list(map(int,input("enter array:").split()))
count=0
for i in a:
    if i>=0:
        count=count+1
print("positive num:",count)