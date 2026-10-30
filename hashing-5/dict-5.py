#count each num num accurance
a=[10,20,10,50,60,1,1,60,8,60,20,60]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
         count[i]=1

        
print(count)


# dict={10:2,30:1,46:5,56:2}
# for value in dict.values():
#     print(value)
# for key,value in dict.items():
#     print(key,value)


# highest value accurance
a=[10,20,10,50,60,1,1,60,8,60,20,60]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
         count[i]=1

print(count)

max_key=0
max_value=0
for key,value in count.items():
    if value>max_value:
        max_value=value
        max_key=key
print(f" highest_count:{max_key}:{max_value}")


# find the duplicate num
a = [10, 20, 10, 30, 20, 40, 50, 10]
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
         count[i]=1
print(count)

duplicate=0

for key,value in count.items():
    if value>1:
        duplicate=key
print(duplicate)
