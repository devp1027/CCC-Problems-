#Dev Patel
#815436
#ICS3U0D
#Formating Output
#Computer Science Club
#03 November 2020
year = int(input("Starting Year: "))
year += 1
year_string = str(year)
str_len = len(year_string)
bool = True

while bool == True:
    counter = 0
    year_string = str(year)
    yearlist = []

    for letter in year_string:
        yearlist.append(letter)

    yearlist2 = yearlist.copy()

    for num in yearlist:
        if (yearlist2.count(num) > 1):
            year += 1
            break
        else:
            counter += 1

    if (counter == str_len):
        bool = False
print (year)
    

