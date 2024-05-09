from operator import itemgetter

def sortAndPrint(listToSort):
    listToSort = sorted(listToSort, key=itemgetter('rank'))
    for rankedCity in listToSort:
        print(f"{rankedCity["rank"]}. {rankedCity["city"]}")


rankedCities = [{"city":"Homestead", "rank": 1}, 
                {"city":"Miami", "rank": 2},
                {"city":"Doral", "rank": 3},
                {"city":"Miami Lakes", "rank": 4},
                {"city":"Coral Gables", "rank": 5},
                {"city":"Fort Lauderdale", "rank": 6}]


print("Here is the list of best cities in South Florida (in order):\n")

sortAndPrint(rankedCities)

print("Disagree? Please enter a city to move:\n")
cityToMove = str(input ("Which city would you like to reposition? "))

selectedDict = {"city": "none", "rank": 0}
for cityDict in rankedCities:
    if cityDict["city"] == cityToMove:
        selectedDict = cityDict.copy()

if selectedDict["city"] == cityToMove:
    newPos = int(input (f"Where would you like to place {cityToMove}? "))
    if (newPos >= 0 and newPos <= len(rankedCities) - 1):
        if selectedDict["rank"] == newPos:
            print(f"{cityToMove} is already in position {newPos}.\n")
        else:
            for cityDict in rankedCities:
                if cityDict["rank"] == newPos:
                    swapDict = cityDict.copy()
                    break
            swapDict["rank"] = selectedDict["rank"]
            selectedDict["rank"] = newPos
            for rankedCity in rankedCities:
                if rankedCity["city"] == swapDict["city"]:
                    rankedCity["rank"] = swapDict["rank"]
                if rankedCity["city"] == selectedDict["city"]:
                    rankedCity["rank"] = selectedDict["rank"]  
    else:
        print("Please select a ranked value in the list.")
else:
    print(f"{cityToMove} was not found in the list!\n")

sortAndPrint(rankedCities)
