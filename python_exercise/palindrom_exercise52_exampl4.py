def palindrome(s):
    word = s.split()
    for i in word:
        if i == i[::-1]:
            print('True')
        else:
            print('False')
