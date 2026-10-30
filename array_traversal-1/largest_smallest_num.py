# largest num

a=[19,34,56,706,8]
largest=a[0]
for num in a:
    if num>largest:
        largest=num
print(largest)

# second largest

a=[12,15,45,6,23,48,56,35]
largest=a[0]
sec_largest=largest
for num in a:
    if num>largest:
        sec_largest=largest
        largest=num
print(largest)
print(sec_largest)


#Count how many times a given number occurs

a=[1,2,3,2,4,2,5]
count=0
target=int(input("enter the target:"))
for num in a:
    if num==target:
        count+=1
print("count:",count)


#smallest
a=[10 ,25 ,3 ,45 ,8,0]
small=a[0]
for i in a:
    if i<small:
        small=i
print(small)

# calculate total sum

num=list(map(int,input("enter array:").split()))
sum=0
for i in num:
    sum=sum+i
print("sum:",sum)