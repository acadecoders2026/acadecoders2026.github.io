s = "xxxxxxxxxxxxxxxxx"
s2 = ""

for i in range(len(s)):
    if i < len(s)/2:
        s2 += str( i + 1 )
    else:
        s2 += str( abs( i - len(s)))



print(s2)
