from PythonDesignPatterns.Creational.Factory.FactoryUseCase.big_chair import BigChair
from PythonDesignPatterns.Creational.Factory.FactoryUseCase.medium_chair import MediumChair
from PythonDesignPatterns.Creational.Factory.FactoryUseCase.small_chair import SmallChair


class ChairFactory:
    @staticmethod
    def get_chair(chair):
        if chair == 'BigChair':
            return BigChair()
        elif chair == 'MediumChair':
            return MediumChair()
        elif chair == 'SmallChair':
            return SmallChair()
        else:
            return None