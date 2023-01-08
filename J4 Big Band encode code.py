#Dev Patel
#815436
#ICS3U0D
#J4 2012 Big Bang 
#Mr.Veera
#20 SEP 2021

shift_value = int(input())
coded = input()
code = []
value_p = 1
for letter in coded:
    let_num = ord(letter)
    if (65<= let_num <= 90):
        new_let_num = let_num - (3 * value_p + shift_value)
        value_p += 1
        if (65<= new_let_num <= 90):
            new_letter = chr(new_let_num)
            code.append(new_letter)
        else:
            if (new_let_num > 90):
                digits_over = new_let_num - 90
                new_dig = digits_over + 66
                code.append(chr(new_dig))
            if (new_let_num < 65):
                digits_over = 65 - new_let_num
                new_dig = 91 - digits_over
                code.append(chr(new_dig))
        if (let_num in range (32,64)):
            code.append(chr(let_num))
        if (let_num in range (91,126)):
            code.append(chr(let_num))
coded_str = ''.join(code)
print (coded_str)

            
            
                
