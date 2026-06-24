class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        right=0
        r=""
        longsum=0
        sub=0
        while right<len(s):
            if s[left] not in r:
                r+=s[right]
                sub+=1
                right+=1
                longsum=max(sub,longsum)
            elif s[left]  in r:
                if left==right:
                    r=s[right]
                    sub+=1
                    right+=1
                    longsum=max(sub,longsum)
                elif left<right:
                    sub=0
                    left+=1
                    r=r[1:]
            
        longsum=max(sub,longsum)
        return longsum