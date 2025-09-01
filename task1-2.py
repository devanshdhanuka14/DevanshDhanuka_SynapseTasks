runes = input("Please enter the runes: ").lower()

check = -1
flag = flag1 = flag2 = flag3 = flag4 = flag5 = 0
step = 0
finalstep = -1

for i in runes:
    step+=1
    if i == "l":
        flag1=1
    elif i == "u":
        flag2=1
    elif i == "m":
        flag3=1
    elif i == "o":
        flag4=1
    elif i == "s":
        flag5=1

    if flag1==1 and flag2==1 and flag3==1 and flag4==1 and flag5==1:
        finalstep = step
        break

print("The number of steps: ",finalstep)






