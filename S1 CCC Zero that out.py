num_of_integers = int(input("How many numbers are there: "))
recorded_nums = []
for i in range(num_of_integers):
    num = (int(input("What is the number: ")))
    if num > 0:
        recorded_nums.append(num)
    if num == 0:
        recorded_nums.pop(-1)
print (sum(recorded_nums))