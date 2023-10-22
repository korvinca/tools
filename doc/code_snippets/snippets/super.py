class Animal(object):
  def __init__(self, animal_type):
    print('Animal Type:', animal_type)
    
class Mammal(Animal):
  def __init__(self):

    # call superclass
    super().__init__('Mammal')
    super().__init__('Boo')
    print('Mammals give birth directly')
    
dog = Mammal()