class Animal():
    def __init__(self,name,color):
        self.name = name
        self.color = color
    
    def sleep(self):
        print(f'{self.name} Zzz...')
    
    def eat(self):
        print(f'{self.name} Om nom nom...')


class Cat(Animal):
    def say(self):
        print(f'{self.name} Meow!!!')

class Dog(Animal):
    def say(self):
        print(f'{self.name} always come back!!!')



fluffy = Cat('snowball','white' )

fluffy.sleep()
fluffy.eat()
fluffy.say()


pg = Dog('afton','purple')

pg.say()