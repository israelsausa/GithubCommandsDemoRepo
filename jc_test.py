class Attribute():
    def __init__(self,strength, speed, intelligence):
        self.strength = strength
        self.speed = speed
        self.intelligence = intelligence

    def power_up (self):
        self.strength *= 5

my_instance = Attribute(10, 15, 20)
print(f"my strength number is {my_instance.strength}")
print(f"my speed number is {my_instance.speed}")
print(f"my intelligence number is {my_instance.intelligence}")

my_instance.power_up()
print(f"my strength number increased! see the power level: {my_instance.strength}")