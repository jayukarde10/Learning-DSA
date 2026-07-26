def palindrome(s, left, right):

    # Base Case
    if left>=right:
        return True

    # Check
    if s[left]==s[right]:
        return palindrome(s, left+1, right-1)
    else:
        return False

s = "jaykaj"
print(palindrome(s, 0, len(s)-1))