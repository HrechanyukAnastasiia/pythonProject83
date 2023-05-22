import random
class Animal:
    def __init__(self, species, name, age, health, hunger, happiness):
        self.species = species
        self.name = name
        self.age = age
        self.health = health
        self.hunger = hunger
        self.happiness = happiness

    def grow(self):
        self.age += 1
        self.health -= random.randint(0, 10)
        self.hunger += random.randint(0, 10)
        self.happiness -= random.randint(0, 10)

    def eat(self):
        if self.hunger >= 10:
            self.health += random.randint(0, 5)
            self.hunger -= random.randint(5, 10)
            self.happiness += random.randint(0, 5)
        else:
            print(self.name, "is not hungry")

    def play(self):
        if self.happiness >= 5:
            self.health += random.randint(0, 5)
            self.hunger += random.randint(0, 5)
            self.happiness += random.randint(0, 5)
        else:
            print(self.name, "does not want to play")

    def __str__(self):
        return f"{self.species} - {self.name} ({self.age} years old)\n" \
               f"Health: {self.health}\nHunger: {self.hunger}\nHappiness: {self.happiness}\n"


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def feed_all(self):
        for animal in self.animals:
            animal.eat()

    def play_with(self, animal):
        if animal in self.animals:
            animal.play()

    def grow_all(self):
        for animal in self.animals:
            animal.grow()

    def __str__(self):
        return "\n".join([str(animal) for animal in self.animals])


def save_zoo_state(zoo, day):
    filename = f"Day_{day}.txt"
    with open(filename, "w") as file:
        file.write(str(zoo))


zoo = Zoo()
zoo.add_animal(Animal("Lion", "Simba", 2, 60, 6, 5))
zoo.add_animal(Animal("Giraffe", "Melman", 4, 80, 8, 7))
zoo.add_animal(Animal("Hippo", "Gloria", 3, 70, 7, 6))

for i in range(1, 11):
    print(f"\nDay {i}")
    save_zoo_state(zoo, i)
    zoo.feed_all()
    random_animal = random.choice(zoo.animals)
    zoo.play_with(random_animal)
    zoo.grow_all()
    print(zoo)

print("\nSimulation finished")