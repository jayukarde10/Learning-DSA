#remove duplicates
arr=[1,2,3,2,1,5,6] 
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)

print(set(arr)) #same but could be in any order

#using set to remove duplicates but maintain order
seen = set()
result = []

for num in arr:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)