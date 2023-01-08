#Dev Patel
#815436
#ICS4U0D
#CCC J5/S2 2014 Assigning Partners
#Mr.Veera
#January 10, 2022

num_students = int(input())                                    #I ask for the number of students in the class 
students_list_one = input().split()                            #I ask for all the names of the first students and split it to create a list with all the individual names of the students
students_lis_two = input().split()                             #I ask for all the names of the first students and split it to create a list with all the individual names of the students
partners = {}                                                  #I make an empty dictionry, in this dictionary all the students will be assigned to thier desingnate partners

#I in this loop I go through both lists of names and assiign them as keys and values to my dictionary.
#The names fromm the first set will be the keys and the names from the reordered set of names will be the values.

for i, k in zip(students_list_one,students_lis_two): 
    partners[i] = k

assingment_check = "Good"                                       #I set the current assingment check to be Good
print ("\n paryners", partners)

#I am interatign through the dictionary of partners. I first get teh value of the current key i am on and set it as the variable "value".
#Then I assingn the varubale name partner two as the name of thier parnter. I then check if the value and key are the same or if partner two does not equal the key.
#If any of these conditions are met then the assingment check will change to Bad and the loop will break

for key in partners:
    value = partners[key]
    student_partner_two = partners[value]
    if (student_partner_two != key or value == key):
        assingment_check = "Bad"
        break
print (assingment_check)                                        #I finally print the assingment check