s="A man, a plan, a canal: Panama"
# s=s.replace(" ", "").lower()  Jay way
# s1=""
# r=""
# for i in s:
#     if ("a"<=i<="z"):
#         s1+=i
#         r=i+r
# if(s1==r):
#     print("its a palindrome")
# else:
#     print("nahh its not")
def isnotc(i):
    return ("a" <= i <= "z") or("0" <= i <= "9")
s=list(s.lower())
left=0
right=len(s)-1
p=True
while left<right:
    if isnotc(s[left]):
        if isnotc(s[right]):
            if s[left]==s[right]:
                p=True
            else:
                p=False
                break
            left+=1
            right-=1
        else:
            right-=1
    else:
        left+=1

if p:
    print("its a palindrome")    
else:
    print("its not")

                
        



