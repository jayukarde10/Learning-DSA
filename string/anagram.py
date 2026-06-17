s1 = "listen"
s2 = "silent"
se1={}
se2={}
for i in range(len(s1)):
    if s1[i] not in se1:
        se1.update({s1[i]: 1})
    else:
        se1.update({s1[i]: se1[s1[i]] + 1})
for i in range(len(s2)):
    if s2[i] not in se2:
        se2.update({s2[i]: 1})
    else:
        se2.update({s2[i]: se2[s2[i]] + 1})
if se1==se2:
    print("its anagram")