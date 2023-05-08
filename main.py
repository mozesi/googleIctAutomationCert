

#Defining a function
def courseStart(name):
    print("You have just enrolled for this course " + str(name))

courseStart("Moses Msukwa")

#convert miles to kilometers

def ConvertDistance(miles):
    km = miles * 1.6
    return km

myTripMiles = 55
myTripKm = ConvertDistance(myTripMiles)
print(myTripKm)