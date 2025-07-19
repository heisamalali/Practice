from PythonDesignPatterns.Creational.Factory.FactoryUseCase.chair_factory import ChairFactory

CHAIR = ChairFactory().get_chair("SmallChair")
print(CHAIR.get_dimension())