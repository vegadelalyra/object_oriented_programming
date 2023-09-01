# https://refactoring.guru/design-patterns/singleton/python/example

# To fix the problem, you have to synchronize threads during the first creation of the Singleton object.

from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
            return cls._instances[cls]
        
class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        pass

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

if __name__ == '__main__':
    print('If you see the same value')
    print('then singleton was reused (yay!)')
    print('If you see diferent values, ')
    print('then 2 singletons were created (boo!!)')
    print('RESULT:')

process1 = Thread(target=test_singleton, args=('FOO',))
process2 = Thread(target=test_singleton, args=('BAR',))

process1.start()
process2.start()