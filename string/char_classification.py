s = "PyThOn@123"
d={'uppercase': '',
   'lowercase':'',
   'digit':'',
   'etc': ''}
left=0
while left<len(s):
    if ('A'<=s[left]<='Z'):
        d['uppercase']+= s[left]
    elif ('a'<=s[left]<='z'):
        d['lowercase']+= s[left]
    elif ('0'<=s[left]<='9'):
        d['digit']+= s[left]
    else:
        d['etc']+= s[left]
    left+=1
print(d)
    
