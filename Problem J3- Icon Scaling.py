#Dev Patel
#815436
#ICS3U0D
#Formating Output
#Mr.Veera
#23 NOV 2020

value_k = int(input())
star_value = ""
value_x = ""
space = ""
for i in range(value_k):
    star_value = star_value + "*"
    value_x = value_x + "X"
    space = space + " "

for i in range (value_k):
    print (star_value + value_x + star_value)
for i in range (value_k):
    print (space + value_x + value_x)
for i in range (value_k):
    print (star_value + space + star_value)
