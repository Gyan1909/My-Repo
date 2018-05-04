with open('test.txt',mode='w') as new_file:
      new_file.write('Hello World')


with open('test.txt',mode='r') as new_file:
     print(new_file.read())
