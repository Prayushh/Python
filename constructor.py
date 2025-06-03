class Person:
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        print("talk")

    

name=input("Enter your name: ")
p1=Person(name)
print(p1.name)
p1.talk()
