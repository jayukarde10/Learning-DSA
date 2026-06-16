#prefix sum array
arr=[10,20,30,40,50]
prefix=[]
n=0
for i in range(len(arr)):
    n=n+arr[i]
    prefix.append(n)
print(prefix)
print(f"sum from index 1 to 4 is {prefix[4]-prefix[0]} ")
print(f"sum from index 0 to 3 is {prefix[3]} ")