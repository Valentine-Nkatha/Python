class Animal: 
  def move(self):
    pass#pass avoids syntax errors and it does nothing when executed
  def make_sound(self):
    pass
class Bird(Animal):
  def move(self):
    print("Flying")
  def make_sound(self):
    print("chirp")
class Cat(Animal):
  def move(self):
    print("running")
  def make_sound(self):
    print("meow")
class Fish(Animal):
  def move(self):
    print("swimming")
  def make_sound(self):
    print("bop")   
                                                   # construcors are not a must if you rae not passing any attributes