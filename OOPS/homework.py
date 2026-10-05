class Animal():
    habitat = "land"

    def __init__(self, species, weight, top_speed):
        self.species = species
        self.weight = weight
        self.top_speed = top_speed

    def eat(self):
        print (self.species, "is eating")

    def sleep(self):
        print (self.species, "is sleeping")

tiger = Animal("Tiger",220,65)
print(tiger.species)
print(tiger.habitat)
print(tiger.weight)
print(tiger.top_speed)

elephant = Animal("Elephant", 5400, 40)
print(elephant.species)
print(elephant.habitat)
print(elephant.weight)
print(elephant.top_speed)

tiger.eat()
tiger.sleep()

elephant.eat()
elephant.sleep()

