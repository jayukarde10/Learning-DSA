#shifting 0 
arr = [0,5,6,0,1,0,0]
count0=0
for i in arr:
    if i==0:
        count0+=1
        arr.remove(i)
        arr.insert(len(arr),0)
    

print(arr)

#Interview Approach (In-Place, Two Pointers) shuffle 0
arr = [0, 1, 0, 3, 12]

pos = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1

print(arr)
#deletion is risky therefor this approch
