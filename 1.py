def count_primes(num): 
    for i in range(num):
        if i < 2:
          break
    for y in range(2,num+1):
        if y % num == 0:
            print('This {} is not prime'.format(y))
        else:
            print(y)
            y = y + 1
    
            
        
            
        
    
    

        
    
