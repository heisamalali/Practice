from interface_chair import IChair

class BigChair(IChair):
    def __init__(self):
        self._height = 80
        self._width = 80
        self._depth = 80

    def get_dimension(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth,
        }