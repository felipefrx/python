class car: #Create an object 
    maxspeed = 0
    on = False
    color = ""

    def __init__(self, m, o, c): #Constructor method 
        self.maxspeed = m
        self.on = o
        self.cor = c

    def show(self):
        status = "On" if c1.on else "Off" #Car status
        print("Maximum speed: {}".format(self.maxspeed))
        print("Color: {}".format(self.color))
        print("On: {}\n".format(status))

    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False
    
    def walk(self):
        if self.on == True:
            print("Walking...")
        else:
            print("Car off.")

c1 = car(250, "Black", True)

c1.maxspeed = 250
c1.color = "Black"
c1.on = True

status = "On" if c1.on else "Off" #Car status

print("Maximum speed: {}".format(c1.maxspeed))
print("Color: {}".format(c1.color))
print("On: {}".format(status))

c2 = car(200, False, "White")
c3 = car(190, True, "Red")

c2.show()
c3.show()

c2.walk()
c3.walk()


class NPC: #Base class, parent class or supler class
    def __init__(self, name, team, force, ammo):
        self.name = name
        self.team = team 
        self.force = force
        self.ammo = ammo
        self.alive = True
        self.energi = 100
    def info(self):
        print("Name: ", self.name)
        print("Team: ", self.team)
        print("Force: ", self.force)
        print("Ammo: ", self.ammo)
        print("Alive: ", "Yes" if self.alive else "Not")
        print("Energi: {}\n".format(self.energi))

class Soldier(NPC): #It inherits all the contents of the NPC class
    def __init__(self, name, team):
        self.force = 200
        self.ammo = 200
        super().__init__(name, team, self.force, self.ammo) #The super method invoke a method or parameter from the parent class 

class Guard(NPC): 
    def __init__(self, name, team):
        self.force = 100
        self.ammo = 20
        super().__init__(name, team, self.force, self.ammo) 

class Elite(NPC): 
    def __init__(self, name, team):
        self.force = 400
        self.ammo = 500
        super().__init__(name, team, self.force, self.ammo) 
    def inf(self):
        super().info()

n1 = Soldier("N1", 1)
n2 = Guard("N2", 2)
n3 = Elite("N3", 3)

n1.info()
n2.info()
n3.inf()