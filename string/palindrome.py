s = "racecar"
pal=""
for i in s:
    pal=i+pal
if pal==s:
    print("palindrome")
else:
    print("its not a palindrome")

#interview version

left=0
right=len(s)-1
while left<right:
    if s[left] != s[right]:
        print("its not a palindrome")

    left+=1
    right-=1

else:
    print("palindrome")