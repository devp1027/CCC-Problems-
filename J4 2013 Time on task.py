with open("problemset.txt", "r") as file:
    total_minutes = int(file.readline())
    total_chores = int(file.readline())
    chores_time = []
    for line in file:
        line = int(line)
        chores_time.append(line)
    chores_time.sort()
    time_counter = 0
    chores_counter = 0
    for n in chores_time:
        if time_counter >= total_minutes:
            break
        if time_counter < total_minutes:
            time_counter += n
            chores_counter += 1
print (total_minutes)
print ("TOTAL TIME", time_counter)
print ("CHORES DONE", chores_counter)
