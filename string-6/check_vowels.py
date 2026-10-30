# count the vowels in the given text
text="python"
count=0
for ch in text:
    if ch in "aeiou":
        count=count+1
print(count)


# count each character

str="banana"
count={}
for i in str:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
