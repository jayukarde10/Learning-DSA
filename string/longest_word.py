s = "I love Python programming"

word = ""
longest = ""

for ch in s:
    if ch != " ":
        word += ch
    else:
        if len(word) > len(longest):
            longest = word

        word = ""

# final comparison for last word
if len(word) > len(longest):
        longest = word
print(longest)