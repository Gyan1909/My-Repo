def animal_crackers(text):
    letter = text.split(" ")
    if letter[0][0].lower() == letter[1][0].lower():
        return True
    else:
        return False
    

