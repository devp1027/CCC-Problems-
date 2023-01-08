switches = int(input("NUMBER OF SWITCHES= "))
on_count = 0
swtich_on = 0
config = []
for i in range (switches):
    OO = int(input("ON OR OFF"))
    config.append(OO)

for on in (config):
    if on_count >= 4:
        print (swtich_on)
        break
    if on == 1:
        on_count += 1
    elif on == 0:
        on_count == 0
        config[on] += 1
        swtich_on += 1
