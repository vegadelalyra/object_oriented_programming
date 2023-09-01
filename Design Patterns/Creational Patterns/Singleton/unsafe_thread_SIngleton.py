# https://refactoring.guru/design-patterns/singleton/python/example

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs): 
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass

if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print('Singleton works, both variables contain the same instance.')
    else:
        print('Singleton failed, variables contain different instances.')

# It’s pretty easy to implement a sloppy Singleton. 
# You just need to hide the constructor 
# and implement a static creation method.

# The same class behaves incorrectly 
# in a multithreaded environment. 
# Multiple threads can call the creation method
# simultaneously and get 
# several instances of Singleton class.