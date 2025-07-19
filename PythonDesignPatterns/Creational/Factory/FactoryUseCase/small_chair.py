from interface_chair import IChair

class SmallChair(IChair):
    def __init__(self):
        self._height = 20
        self._width = 20
        self._depth = 20

    def get_dimension(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth,
        }