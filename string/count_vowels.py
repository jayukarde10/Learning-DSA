s=input("enter a word")
vow={"a","e","i","o","u"}
count=0
for i in s:
    if i in vow:
        count+=1

print(count)