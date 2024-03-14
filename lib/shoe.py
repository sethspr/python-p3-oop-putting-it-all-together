#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size #we do not type self._size with underscore here, becuase it bypasses the setter. 
        self.condition = None #default value of None becuase we do not have any info on the shoe condition. 

    def __repr__(self):
        return f"<Brand: {self.brand}, Size: {self._size}>"
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size_int):
        if type(size_int) == int:
            self._size = size_int
        print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
    # When the cobble method is called, it sets the condition to "New", indicating that the shoe has been repaired and is now in a new condition.

   
my_shoe = Shoe("Adidas", 9)

print(my_shoe)