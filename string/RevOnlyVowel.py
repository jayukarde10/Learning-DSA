se="leecode" #['l', 'e', 'e', 'c', 'o', 'd', 'e']
s=[] 
for i in se: #optimization s=list(se)
    s.append(i)

vowel="aeiou"
left=0
right=len(s)-1
while left<right:
    if s[left] in vowel:
        if s[right] in vowel:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        else:
            right-=1
    else:
        left+=1

s2="" 
for i in s: #optimization s2="".join(s)
    s2+=i        
    
print(s2)

