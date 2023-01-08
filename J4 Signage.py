def sign(pharse,w): 
    new_sign=[]
    while (len(pharse)>0):
        row=[] 
        position=0 
        length=0 
        while ((position<len(pharse)) and (length+len(pharse[position])<=w)): 
            row.append(pharse[position]) 
            length+=len(pharse[position]) 
            position+=1 
            if ((position<len(pharse) and (length+1+len(pharse[position])<=w))):
                row.append('.') 
                length+=1
            else:
                break 
        if (len(row)==1) and (length!=w): 
            row.append('.')
            length+=1 
        pharse=pharse[position:] 
        remaining=w-length 
        while (remaining>0): 
            for position in range(1,len(row),2): 
                if (remaining<=0): 
                    break
                row[position]+='.' 
                remaining-=1
        new_sign.append(row)
    return new_sign
 
w=int(input('Enter w: '))
pharse=['WELCOME','TO','CCC','GOOD','LUCK','TODAY']
new_sign=sign(pharse,w)
for row in new_sign:
    print(''.join(row))