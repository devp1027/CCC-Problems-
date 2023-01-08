#with open("testcase1.txt","r") as file:
#    content = file.read()
content = list("MSL")
print (content)
new = sorted(content)
count = 0
zip_object = zip(content, new)
for element1, element2 in zip_object:
    if element1 != element2:
        count += 1
count = count / 1.6
print (round (count))