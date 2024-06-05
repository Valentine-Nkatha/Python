class Vehicle:
    def __init__(self,make,color):
        self.make=make
        self.color=color

    def accelerate(self):
         print("acceleration started")
    def hoot(self):
         print("hoot hoot")
class Bus(Vehicle):
    def __init__(self,make,color,passengers):
        super().__init__(make,color)
        self.passengers=passengers 
    def start_boarding(self):
        print("The bus is boarding")     
    
class Lorry(Vehicle):
        def __init__(self,make,color,max_load):
            super().__init__(make,color)
            self.max_load=max_load

        def unload(self):
            print("unloading")


        