cityList = ["Homestead", "Miami", "Doral", "Miami Lakes", "Coral Gables", "Fort Lauderdale"]

print("Here is the list of best cities in Miami-Dade (in order):\n")

for i in range(len(cityList)):
    print(f"{i+1}. {cityList[i]}")

print("Disagree? Please enter a city to move:\n")
cityToMove = str(input ("Which city would you like to reposition? "))

if cityToMove in cityList:
    newPos = int(input (f"Where would you like to place {cityToMove}? "))
    if (newPos >= 0 and newPos <= len(cityList) - 1):
        if cityList[newPos-1] == cityToMove:
            print(f"{cityToMove} is already in position {newPos}.")
        else:
            cityList.remove(cityToMove)
            cityList.insert(newPos-1, cityToMove)
    else:
        print("PLease select a value within the range of the list.")
else:
    print(f"{cityToMove} was not found in the list!\n")

print("\n")
for i in range(len(cityList)):
    print(f"{i+1}. {cityList[i]}")