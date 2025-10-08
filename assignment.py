class Dog:
    def __init__(self,breed, color):
        self.breed=breed
        self.color=color

    def animal(self):
        print(f"The breed of this dog is {self.breed} and its color is {self.color}.")

ob1= Dog("Golden Retriever", "Cream/Golden")
obj2= Dog("German Shepherd","Black,Brown" )
print(ob1.animal())
print(obj2.animal())



