#Dev Patel
#815436
#ICS4U0D
#CCC J3 2021 Speical Insturctions
#Mr.Veera
#Sep 20 2021

previous_direction = ''
outputs=[]
while True:
    current=input()
    if current=='99999':
        break
    current=list(current)
    digit_sum=int(current[0])+int(current[1])
    if digit_sum == 0:
        direction = previous_direction
    elif digit_sum%2==1:
        direction="left"
    elif digit_sum%2==0:
        direction="right"      
    direction_string = direction+' '+str(''.join(current[2:]))
    outputs.append(direction_string)
    previous_direction = direction
    if direction == '':
        break
    print (direction_string)
