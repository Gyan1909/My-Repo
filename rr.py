def count_primes(num):
  for i in range(num):
   # prime numbers are greater than 1
   if i > 1:
       for y in range(2,i):
           if (i % y) == 0:
               break
       else:
           print(i)
