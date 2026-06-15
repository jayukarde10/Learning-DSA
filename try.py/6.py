arr = [1, 2, 3, 4, 6]
target = 6
n=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        n=arr[i]+arr[j]
        if n==target:
            print(f"{arr[i]}+{arr[j]}={target}")
            break
