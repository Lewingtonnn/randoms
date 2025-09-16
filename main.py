left,right= 1,22
output=[]

while right>0:
    digit=right%10
    if right%digit==0 and digit!=0:
        output.append(digit)
    right=right//10
    print(output)

while left>0:
    digit=right%10
    if digit==0:
        break
    if right%digit==0 and digit!=0:
        output.append(digit)
    right=right//10
    print(output)