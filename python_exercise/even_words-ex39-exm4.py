st = 'Print every word in this sentence that has an even number of letters'
letter = st.split(" ")
for words in letter:
    if len(words)%2 == 0:
        print(words + ' is even!')
        
