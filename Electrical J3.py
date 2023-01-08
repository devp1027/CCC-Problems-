#Dev Patel
#815436
#Exactly Electrical
#Computer Science Club
#Nov 13 2020

start = input("Starting point (x y): ")
end = input("Ending point (x y): ")
charge = int(input("How charged is your battery? (Must be above 0): "))

start = start.split()
end = end.split()

Value_X_start = int(start[0])
Value_Y_start = int(start[1])

Value_X_end = int(end[0])
Value_Y_end = int(end[1])
 
distance_x = Value_X_end - Value_X_start
distance_y = Value_Y_end - Value_Y_start

distance = distance_x + distance_y

if (charge == abs(distance)):
    print ("Y")

if (charge % 2 == 0 and abs(distance) % 2 == 0):
    print ("Y")
if (charge % 2 != 0 and abs(distance) % 2 != 0):
    print ("Y")
else:
    print ("N")
