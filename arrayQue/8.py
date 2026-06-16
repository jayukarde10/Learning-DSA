#sliding window
arr = [1,4,2,10,23,3,1,0,20]
k = 4
window=sum(arr[:k])
maxwindow=window
for i in range(k,len(arr)):
    window=window-arr[i-k]+arr[i]

    if window>maxwindow:
        maxwindow=window

print(maxwindow)

