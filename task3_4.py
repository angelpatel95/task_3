def leap(year):
    leap = False
    if year % 400 == 0:
        leap = True
    elif year % 4 == 0:
        leap = True
    return print(leap)
    
leap(2013)
