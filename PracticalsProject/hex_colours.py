colours = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "BEIGE": "#f5f5dc", "BLACK": "#000000",
           "BlANCHEDAlMOND": "#ffebcd", "CHOCOLATE": "#d2691e", "BLUEVIOLET": "#8a2be2", "BROWN": "#a52a2a",
           "BURLYWOOD": "#deb887", "CADETBLUE": "#5f9ea0"}
print(colours.keys())

user_colours = input("Please enter the colour that you want to search: ").upper()
print("If you want to stop, type a blank")
while user_colours != ' ':
    if user_colours in colours:
        print(user_colours, "is", colours[user_colours])
        break
    else:
        print('Invalid enter')
        user_colours = input("Please enter the colour that you want to search: ").upper()