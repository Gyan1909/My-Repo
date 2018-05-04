def up_low(s):
    total = 0
    total_upper = 0
    for i in s:
        if i.isupper(): 
          total_upper+=1
        elif i.islower():
            total+=1
        else:
           pass
    print("Original String:",s)
    print("No. of Upper case characters: ", total_upper)
    print("No. of lower case characters: ", total)
