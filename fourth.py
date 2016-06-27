# Create a Rocket class
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9"
# 2nd parameter: the starting fuel level as a number
# 3rd parameter: number of launches as a number

class Rocket:

    def __init__ (self, rocket, fuel, launches):
        self.rocket = rocket
        self.fuel = fuel
        self.launches = launches

    def launch(self):
        if self.rocket == 'falcon1':
            self.fuel = self.fuel - 1
            self.launches = self.launches + 1
            return self.fuel
        if self.rocket == 'falcon9':
            self.fuel = self.fuel - 9
            self.launches = self.launches + 1
            return self.fuel

    def refill(self):
        usedFuel = 0
        if self.rocket == 'falcon1':
            usedFuel = 5 - self.fuel
            self.fuel = 5
            return usedFuel
        if self.rocket == 'falcon9':
            usedFuel = 20 - self.fuel
            self.fuel = 20
            return usedFuel

    def getStats(self):
        return 'name: ' + self.rocket + ', ' + 'fuel: ' + str(self.fuel)


rocket1 = Rocket('falcon1', 5, 1)
print(rocket1.launch())
print(rocket1.refill())
print(rocket1.getStats())

rocket2 = Rocket('falcon9', 20, 1)
print(rocket2.launch())
print(rocket2.refill())
print(rocket2.getStats())

class SpaceX:

    def __init__ (self, fuel):
        self.fuel = fuel

    def addRocket(self, rocket):
        allRockets = ''
        self.rocket = rocket
        allRockets += self.rocket
        return allRockets

    def refill_all(self):
        x = self.addRocket(self.rocket)
        rocket1.refill()
        rocket2.refill()

spacex1 = SpaceX(100)
print(spacex1.addRocket('falcon1'))
print(spacex1.refill_all())

spacex2 = SpaceX(100)
print(spacex2.addRocket('falcon9'))
print(spacex2.refill_all())

# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 if it's a falcon9
# it should increment the launches by one
#
# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9
# it should return the used fuel
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2
#
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11"

# Create a SpaceX class
# it should take 1 parameter in its constructor
# 1st parameter: the stored fuel
#
# it should have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter
#
# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage
#
# launch_all()
# it should launch all the rockets
#
# buy_fuel(amount)
# it should increase stored fuel by amount
#
# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"


# The following code should work with the classes


#space_x = SpaceX(100)
#falcon1 = Rocket('falcon1', 0, 0)
#falcon9 = Rocket('falcon9', 0, 0)
#returned_falcon9 = Rocket('falcon9', 11, 1)

#print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

#space_x.addRocket(falcon1)
#space_x.addRocket(falcon9)
#space_x.addRocket(returned_falcon9)

#print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
#space_x.refill_all()
#print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
#space_x.launch_all()
#print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
#space_x.buy_fuel(50)
#print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
