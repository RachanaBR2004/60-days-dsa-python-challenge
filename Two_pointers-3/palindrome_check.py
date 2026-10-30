a=[1,2,3,4,5]
left=0
right=len(a)-1
while left<right:
    # a[left]=a[right]
    # a[right]=a[left]
    a[left], a[right] = a[right], a[left]  
    left+=1
    right-=1
print("reversed array",a)



# check wheather the array is palindrome and not palindrome 
b=[1,2,4,4,2,1]
left=0
right=len(b)-1
is_palindrome=True
while left<right:
   if b[left]!=b[right]:
    is_palindrome=False
    break
   left+=1
   right-=1
if is_palindrome==False:
    print(" not palindrome")
else:
    print("palindrome")


# target prblm

a=[1,2,3,4,6,7,8,9]
target=int(input("enter the target:"))
left=0
right=len(a)-1
found=False
while left<right:
   if a[left]+a[right]==target:
      found=True
      break
   elif a[left]+a[right]>target:
      right-=1
   else:
      left+=1
 
if found==True:
   print("it is available")
else:
   print("it is not available")
      



