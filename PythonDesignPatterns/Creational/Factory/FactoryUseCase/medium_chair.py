from interface_chair import IChair

class MediumChair(IChair):
    def __init__(self):
        self._height = 50
        self._width = 50
        self._depth = 50

    def get_dimension(self):
        return {
            "width": self._width,
            "height": self._height,
            "depth": self._depth,
        }