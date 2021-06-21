
class AT_Coord:
    def __init__(self, nbr_coord):
        self.__coord = []
        if nbr_coord > 0:
            for i in range(nbr_coord):
                self.__coord.append(0.0)

    def getCoord(self, indice):
        if indice >= 0 and indice < len(self.__coord):
            return self.__coord[indice]
        return None

    def setCoord(self, indice, value):
        if indice >= 0 and indice < len(self.__coord):
            self.__coord[indice] = value

    def getCopy(self):
        copy_ = AT_Coord(len(self.__coord))
        copy_.__coord = self.__coord.copy()

        return copy_

class Vector2D(AT_Coord):
    def __init__(self, x=0.0, y=0.0):
        AT_Coord.__init__(self, 2)
        AT_Coord.setCoord(self, 0, x)
        AT_Coord.setCoord(self, 1, y)

    def getX(self):
        return super().getCoord(0)

    def getY(self):
        return super().getCoord(1)

    def setX(self, value):
        super().setCoord(0, value)

    def setY(self, value):
        super().setCoord(1, value)

    def __str__(self):
        return "Vector({}, {})".format(self.getX(), self.getY())

class Size2D(AT_Coord):
    def __init__(self, w=0.0, h=0.0):
        AT_Coord.__init__(self, 2)
        self.setCoord(0, w if w >= 0.0 else -w)
        self.setCoord(1, h if h >= 0.0 else -h)

    def getW(self):
        return super().getCoord(0)

    def getH(self):
        return super().getCoord(1)

    def setW(self, value):
        super().setCoord(0, value)

    def setH(self, value):
        super().setCoord(1, value)

    def __str__(self):
        return "Size({}, {})".format(self.getW(), self.getH())