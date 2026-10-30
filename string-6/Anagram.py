text1="listen"
text2="silent"
count1={}
count2={}
for i in text1:
    if i in count1:
        count1[i]=count1[i]+1
    else:
        count1[i]=1

for i in text2:
    if i in count2:
        count2[i]=count2[i]+1
    else:
        count2[i]=1

print(count1)
print(count2)

if count1==count2:
    print("anagram")
else:
    print("not anagram")




