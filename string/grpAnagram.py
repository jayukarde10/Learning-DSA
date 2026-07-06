l=["eat", "tea", "tan", "ate", "nat", "bat"]
d={}
for i in l:
    s="".join(sorted(i))
    if s not in d:
        d.update({s:[i]})
    else:
        d[s].append(i)
print(d)

