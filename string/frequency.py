#count frequency of each character in a string
s="aabfbcdde"
se={}
for i in range(len(s)):
    if s[i] not in se:
        se.update({s[i]: 1})
    else:
        se.update({s[i]: se[s[i]] + 1})
print(se)
#find first non repeating character
for i in s:
    if se[i]==1 :
        print(f"{i} is first non repeating")
        break
