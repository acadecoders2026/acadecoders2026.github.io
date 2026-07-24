s=''
p = ' '


#_________1
#________121


# 12 1
# 12321
size = 9
top_half = []
for i in range(size):
    line = p * (size - i)
    numbers = ''
    for  j in range(1, i+1):
        numbers += str(j)
    for k in range(i-1, 0, -1):
        numbers += str(k)

    line += numbers

    top_half.append(line)

for line in top_half:
    print(line)
for i in range(len(top_half), 0, -1):
    print(top_half[i-1])

    #FLAG{"lambda_x:_x.secret()"}


