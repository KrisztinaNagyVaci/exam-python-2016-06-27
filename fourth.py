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
            return self.fuel
        if self.rocket == 'falcon9':
            self.fuel = self.fuel - 9
            return self.fuel


rocket1 = Rocket('falcon1', 3, 2)
print(rocket1.launch())

rocket2 = Rocket('falcon9', 10, 2)
print(rocket2.launch())

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
