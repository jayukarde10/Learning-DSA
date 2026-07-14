s="abbcaa"
left=0
right=1
count=1
result=""
while left<len(s)-1:
    if s[left]==s[right]:
        count+=1                    #Jay Logic is right but fail for null string only 
        left+=1
        right+=1
        
    else:
        result+=s[left]+str(count)
        count=1
        left+=1
        right+=1
result+=s[right-1]+str(count)

print(result)

#perfect
s = "abbcaa"

if not s:
    print("")
else:
    result = ""
    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1

    # Add the last group
    result += s[-1] + str(count)

    print(result)