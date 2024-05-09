rankedCities = [{"city":"Homestead", "rank": 1}, 
                {"city":"Miami", "rank": 2},
                {"city":"Doral", "rank": 3},
                {"city":"Miami Lakes", "rank": 4},
                {"city":"Coral Gables", "rank": 5},
                {"city":"Fort Lauderdale", "rank": 6}]

print("Here is the list of best cities in South Florida (in order):\n")

for rankedCity in rankedCities:
    print(f"{rankedCity["rank"]}. {rankedCity["city"]}")

print("Disagree? Please enter a city to move:\n")
cityToMove = str(input ("Which city would you like to reposition? "))

selectedDict = dict()
for cityDict in rankedCities:
    if cityDict["city"] == cityToMove:
        selectedDict = cityDict.copy()

if selectedDict["city"] == cityToMove:
    newPos = int(input (f"Where would you like to place {cityToMove}? "))
    if (newPos >= 0 and newPos <= len(rankedCities) - 1):
        if selectedDict["rank"] == newPos:
            print(f"{cityToMove} is already in position {newPos}.")
        else:
            # Need to find the other one
            cityList.remove(cityToMove) #this is old code
            cityList.insert(newPos-1, cityToMove) # this is old code
    else:
        print("Please select a value within the range of the list.")
else:
    print(f"{cityToMove} was not found in the list!\n")

