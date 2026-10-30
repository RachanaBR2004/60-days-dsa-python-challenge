a=[10,20,10,40,30,40,20,2,3]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

for key,value in count.items():
    if value==1:
        print(key)
        break
    


