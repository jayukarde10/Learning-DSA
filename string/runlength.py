s="aaaabbbbccaa"
d={}
left=0
count=0
se=[]
while left<len(s):
    if s[left]  in se:
        count+=1  
        d[se[0]]=count  
    else:
        se=[]
        se.append(s[left])
        count=0
        count+=1
        d[se[0]]=count
    left+=1

print(d)
