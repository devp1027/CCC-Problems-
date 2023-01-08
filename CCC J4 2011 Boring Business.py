#Dev Patel
#815436
#ICS4U0
#CCC J4 2011 Boring Business
#Mr.Veera
#23 SEP 2021

x=-1  #The 2 varibles are the x and y coordinates that the drill is currently on. These x and y cooridate will increase or decrease based upon the users inputs
y=-5

output=[] #This is a list that will store the outputs produced by my function. It will provide a new coordinate and whetehr it is safe or dangerous
current_path = [[0,-1],[0,-2],[0,-3], [1,-3],[2,-3],[3,-3], [3,-4], [3,-5],\
                [4,-5],[5,-5],[5,-4],[5,-3],[6,-3],[7,-3],[7,-4],[7,-5],[7,-6],[7,-7],\
                [6,-7],[5,-7],[4,-7],[3,-7],[2,-7],[1,-7],[0,-7],[-1,-7],[-1,-6],[-1,-5]] #This is a 2D list that stores all the current coordinats that the drill has passed. Once a new coordinate is made it will be added to this list

drill_status="Safe" #This simplies initializes the varible drill status to safe. This tells the program that currently the drill is in a safe location. 

while (drill_status!="DANGER"): #This is a while loop that loops through until the varbile drill status is equal to dangerous
    direction_len=input('Enter the direction (u, d, r or l) followed by the positive length: ').split()  #I am asking for the user to input the direction that they want the drill to move and the length they want to move it. I have added the function .spilt, which will spilt the string input into a list.
    direction=direction_len[0] #This is a simple varible that sets the direction of tht drill to the first index of the input by the user
    length=int(direction_len[1]) #This is the same varible as the one above however, it is initalizing the length as a intger. 
    error_check = False #This varible that is currently set to true. It has been made to check if there are errors in the length input.
    if (direction == "d") and ((y-length)<-200): #This is an error checker for if the drill goes under the ground by more then 200 units
        print ("\nInvalid length. Length goes beyond 200 units down.")
        error_check = True
    elif (direction == "u") and ((y+length)>=0): #This is an error checker for if the drill goes over the surface
        print ("\nInvalid length. Length goes above ground.")
        error_check = True
    elif (direction == "l") and ((x-length)<-200): #This is an error checker for if the drill goes to the left by more then 200 units
        print ("\nInvalid length. Length goes beyond 200 units left.")
        error_check = True
    elif (direction == "r") and ((x+length)>200): #This is an error checker for if the drill goes to the right by more then 200 units
        print ("\nInvalid length. Length goes beyond 200 units right.")
        error_check = True
    if error_check == True: #This if statment checks if the error check is true and breaks the loop if it is.
        break
    
    if direction=="q": #This checks if the direction enetered is q as if it is it will stop the loop and break out of the loop
        break

    for i in range(length): #This is a for loop that loops through the length of the function times. This is will add 1 to the x or y coordinate the appropritate amount of times as the user wants. 
        if direction=="u": #This is a if statement that checks for the letter that is stored in the varible direction. If the letter is u it means that the drill will be going up and increasing the y-value by one
            y+=1
        elif direction=="d":  #This is a if statement that checks for the letter that is stored in the varible direction. If the letter is d it means that the drill will be going down and decreasing the y-value by one
            y-=1
        elif direction=="r":  #This is a if statement that checks for the letter that is stored in the varible direction. If the letter is r it means that the drill will be going to the right and increasing the x-value by one.
            x+=1
        elif direction=="l": #This is a if statement that checks for the letter that is stored in the varible direction. If the letter is l it means that the drill will be going to the left and decreasing the x-value by one.
            x-=1
        if [x,y] in current_path: #Once the new x and y coordinates have been initialized the programs checks the main list for if the coordinates pre-exsit. If they do the program will tell the user that it is dangerous as the area has already been drilled.
            drill_status="DANGER"
        else:
            current_path.append([x,y]) #However, if the X and Y coordinates are not pre-existing in the list, it will store this new X and Y coordinate in the list
    new_coord = "{} {} {}".format(x,y,drill_status) #This formats a string to display the x and y coordiante with the status of the drill, if it is dangerous or if it is safe.
    output.append(new_coord) #This stores the new string into the output list.

for i in output: #This is a for loop that goes through the output list and prints every string stored in the list.
    print (i)
