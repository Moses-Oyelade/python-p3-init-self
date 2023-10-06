#!/usr/bin/env python3

# class Dog:
#     pass
#     def __init__(self, name, favorite_toy="Any"):
#         self.name = name
#         self.favorite_toy = favorite_toy
#         # print(f"{name} is born!")
        
#     def bark(self):
#         print("Woof!")
        
#     def showing_self(self):
#         return self
    
#     def get_adopted(self, owner_name):
#         self.owner = owner_name
    
        
    
# fido = Dog("Fido")
# # print(fido.name)
# snoopy = Dog("Snoopy", "Tennis Ball")
# print(snoopy.name)

# # fido.owner = "Sophie"
# fido.get_adopted("sophie")
# print(fido.owner)

# print(fido.favorite_toy)
# print(snoopy.favorite_toy)


class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name=name
        self.breed=breed
        
        
jack = Dog("Jack")
print(f"Dog name: {jack.name}")
print(f"Dog breed: {jack.breed}")