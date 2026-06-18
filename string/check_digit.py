s = "12a82"

for ch in s:
    if ch < '0' or ch > '9':
        print("Not Only Digits")
        break
else:
    print("Only Digits")