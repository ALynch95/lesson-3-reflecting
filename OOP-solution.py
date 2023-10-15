class Pod_Racer:
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def repair(self):
        self.condition = 'repaired'

    
class Anakin_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = 'Anakin'):
        super().__init__(max_speed, condition, price, owner)

    def boost(self):
        self.max_speed *=2

class Sebulba_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = 'Sebulba'):
        super().__init__(max_speed, condition, price, owner)

    def flame_jet(self, other_pod):
        print( 'flaming', other_pod.owner)
        other_pod.condition = 'trashed'

anakins_pod = Anakin_Pod(25, 'perfect', 1000)

sebulbas_pod = Sebulba_Pod(28, 'perfect', 1000000)

print('anakins condition', anakins_pod.condition)
print('sebulbas condition', sebulbas_pod.condition)

sebulbas_pod.flame_jet(anakins_pod)

print('anakins condition', anakins_pod.condition)
print('sebulbas condition', sebulbas_pod.condition)

print('anakins max speed', anakins_pod.max_speed)
print('sebulbas max speed', sebulbas_pod.max_speed)

anakins_pod.boost()

print('anakins max speed', anakins_pod.max_speed)
print('sebulbas max speed', sebulbas_pod.max_speed)



'''
How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    Encapsulation: The classes encapsulate data and behavior, hiding data attributes and enabling methods like repair to manage the data.
    Inheritance: Anakin_Pod and Sebulba_Pod inherit from Pod_Racer, reusing its attributes and methods while adding their own.
    Polymorphism: boost and flame_jet methods provide different implementations for the same method name, demonstrating polymorphism.
    Abstraction: The design abstracts common pod racer attributes and behaviors into a base class, making it easier to manage specific 
    instances with distinct characteristics.

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
    Using a different coding style, such as procedural programming, would likely result in less organized, less maintainable,
    and less readable code for this problem. Object-Oriented Programming provides a structured and intuitive way to model and manage pod racers,
    making it the more suitable choice.

How in particular did Object Oriented Programming assist in the solving of this problem?
    OOP helped solve this problem by structuring the code, encapsulating data, enabling code reuse through inheritance,
    implementing polymorphism, and abstracting complexities, making the code more manageable and intuitive.

'''