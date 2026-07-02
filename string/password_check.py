s=str(input("enter a password"))
c={"has_upper" :False,
"has_lower" : False,
"has_digit" : False,
"has_special" :False,
}

if (len(s)>=8):
    for i in s:
        if ('A'<=i<='Z'):
            c["has_upper"]=True
        elif ('a'<=i<='z'):
            c["has_lower"]=True
        elif ('0'<=i<='9'):
            c["has_digit"]=True
        else:
            c["has_special"]=True
else:
    print("length of password atleast should be 8")
    
if (
    c["has_upper"] and
    c["has_lower"] and
    c["has_digit"] and
    c["has_special"] 
):
    print("Strong Password")
else:
    print("Weak Password")

    
        



