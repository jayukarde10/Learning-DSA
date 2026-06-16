#Kadane's Algorithm
arr=[-2,1,-3,4,-1,2,1,-5,4]
maxsum=arr[0]
curentsum=arr[0]

for i in range(1,len(arr)):
    curentsum=max(arr[i],curentsum+arr[i])
    maxsum=max(maxsum,curentsum)

print(maxsum)