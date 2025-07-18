from abc import ABC, abstractmethod
# using ABC is more modern than metaclass=ABCMeta
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        pass

class Dog(Animal):
    def speak(self):
        print('Dog')

dog = Dog()
dog.speak()