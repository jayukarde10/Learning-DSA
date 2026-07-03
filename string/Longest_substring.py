s = "pwwkew"

seen = set()

left = 0
maxlen = 0

for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left]) #Imp 
        print("remove",seen)#to check by jay
        left += 1 #while loop will keep removing until the condition is false

    seen.add(s[right])
    print("add",seen)#to check by jay

    maxlen = max(maxlen, right - left + 1)
    # maxlen = max(maxlen, len(seen)) is also correct

print(maxlen)