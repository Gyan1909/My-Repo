def print_big(letter):
    patterns= {1:'*',2:'* *',3:'***',4:'****',5:'*****' }
    alphabets = { 'A':[1,3,4,3,3],'B':[6,4,6,4,6]}
    for pattern in alphabets[letter.upper()]:
        print(patterns[pattern])

            

            


        
