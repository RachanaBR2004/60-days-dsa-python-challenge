#Find the first character that appears only once.

text = "programming"
count={}
for i in text:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)

for key,value in count.items():
    if value==1:
        print(key)
        break

