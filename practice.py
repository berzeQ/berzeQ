class dog:
    species= 'mongol'
    def __init__ (self, name, age):
        self.name = name
        self.age=age
        
    def bark(self):
        return f"{self.name} is barking"
    def walk(self):
        return f'thanks for taking {self.name} for a walk. uWu'
    
my_dog=dog('Kale', 5)

print(my_dog.bark())
# Output: Kale is barking
print(my_dog.name)
print(my_dog.age)

class puppy(dog):
    def play(self):
        return f"{self.name} is playing"
    def bite(self):
        return f"{self.name} is biting"
class cat(puppy):
    def meow(self):
        return f"{self.name} is meowing"
    
my_puppy = puppy('runche', 10)
print(my_puppy.play())
print(my_puppy.age)
print(my_puppy.species)
print(my_puppy.walk())
print(my_puppy.bite())
my_cat = cat('kitty', 2)
print(my_cat.meow())

print(my_cat.play())