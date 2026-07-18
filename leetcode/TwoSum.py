nums=[2,7,11,15]
target=9

for i in range(len(nums)):  #my logic is right but  complexity is O(n^2)
    for j in range(i+1,len(nums)):
         if nums[i]+nums[j]==target:
            print([i,j])
            break

#chatgpt

hashmap = {}

for i, num in enumerate(nums):
    complement = target - num

    if complement in hashmap:
        print([hashmap[complement], i])

    hashmap[num] = i




# for i, num in enumerate(nums):
#     print(i, num)

# Output:

# 0 2
# 1 7
# 2 11
# 3 15