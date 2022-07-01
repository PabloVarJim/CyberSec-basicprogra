#Calculation of the distance from home to the University
#Calculation of the cost per kilometer
#Calculaiton of the amount of days you visit the University
#Calculation of the total cost in a four-months period

Distance =  int(input("Distance in kilometers : "))
Kilometer_cost = int(input("Kilometer_cost : "))
Amount_of_visits = int(input("Amount_of_visits : "))

#Calculation of distance per cost times the amount of visits to the University

print ("Total cost of visits to the University per a four month period is: ")
print(Distance * Kilometer_cost * Amount_of_visits * 15)
