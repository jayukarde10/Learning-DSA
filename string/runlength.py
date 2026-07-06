s="aaaabbbbcc"
d={}

for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
        
result=""
for i in d:
    result+= i + str(d[i])
print(result)