s="bananannn"
d={}

for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1 

c=0

mcr=""
for i in d:
    if d[i]>c:
        c=d[i]
        mcr=i
       
print(mcr)