cityList = ["Homestead", "Miami", "Doral", "Miami Lakes", "Coral Gables", "Fort Lauderdale"]

print("Here is the list of cities:\n")
for city in cityList:
    print(city)

print("\n")
cityToDel = str(input ("Please enter a city to remove from the above list: "))

if cityToDel in cityList:
    cityList.remove(cityToDel)
    print(f"{cityToDel} has been removed from the list\n")
else:
    print(f"{cityToDel} was not found in the list\n")

for city in cityList:
    print(city)