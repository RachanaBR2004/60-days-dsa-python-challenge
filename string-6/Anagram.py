# text1="listen"
# text2="silent"
# count1={}
# count2={}
# for i in text1:
#     if i in count1:
#         count1[i]=count1[i]+1
#     else:
#         count1[i]=1

# for i in text2:
#     if i in count2:
#         count2[i]=count2[i]+1
#     else:
#         count2[i]=1

# print(count1)
# print(count2)

# if count1==count2:
#     print("anagram")
# else:
#     print("not anagram")






s = "rat"
t = "car"
scount={}
tcount={}
for ch in s:
    if ch in scount:
        scount[ch]+=1
    else:
        scount[ch]=1
print(scount)
    
for i in t:
    if i in tcount:
        tcount[i]+=1
    else:
        tcount[i]=1
print(tcount)


if scount==tcount:
    print("True")
else:
    print("False")
            
        
        



        
        