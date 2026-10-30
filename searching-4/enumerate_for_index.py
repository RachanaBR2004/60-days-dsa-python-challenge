
# want to find index
a=[10 ,20 ,30 ,40 ,50]
search=int(input("enter the num:"))
flag=False
for index, i in enumerate(a):
    if search==i:
        flag=True
        found_index=index
if flag==True:
    print(f"index of num:\nsearch:{search},index:{found_index}")




# first accurance

a = [10, 20, 30, 20, 40, 20]
search=int(input("enter the name:"))
flag=False
for index,i in enumerate(a):
    if search==i:
        flag=True
        found_index=index
        break
if flag==True:
    print(f"index:{found_index},search:{search}")