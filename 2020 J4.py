text = input().split()
shift = list(input())
while True:
    shift = ' '.join(shift)
    if shift in text:
        print ("Yes")
        break
    else:
        shift = list(shift)
        shift.append(shift.pop(0))
        shift = str(shift)
        print (shift)