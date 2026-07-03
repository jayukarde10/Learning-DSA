#sliding window
s = "educatioan"
k = 3

vowels = "aeiou"

# Count vowels in the first window
current = 0
for i in range(k):
    if s[i] in vowels:
        current += 1

maximum = current

# Slide the window
for i in range(k, len(s)):

    # Character leaving the window
    if s[i-k] in vowels:
        current -= 1

    # Character entering the window
    if s[i] in vowels:
        current += 1

    maximum = max(maximum, current)

print(maximum)

# # Jay's try this is not a sliding window 
# s = "education"
# k = 4
# l=0
# r=len(s)
# v=["a","e","i","o","u"]
# count=0
# maxcount=0
# while k <= len(s):
#     w=s[l:k]
#     for i in w:
#         if i in v:
#             count+=1
#     maxcount=max(count,maxcount)
#     count=0
#     l+=1
#     k+=1
# maxcount=max(count,maxcount)
# print(maxcount)
