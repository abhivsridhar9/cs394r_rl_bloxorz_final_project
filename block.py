import numpy as np


class Block:

    def __init__(self, xr, c1, r2, c2):
        self._r1 = r1
        self._r2 = r2
        self._c1 = c1
        self._c2 = c2

    def set_coords(self, r1, c1, r2, c2):
        self._r1 = r1
        self._r2 = r2
        self._c1 = c1
        self._c2 = c2

    def get_coords(self):
        return np.ndarray([self._r1, self._r2, self._c1, self._c2])

    def isUpright(self):
        if self._r1 == self._c1 and self._r2 == self._c2:
            return True

        return False

    def isWide(self):
        if self.isUpright:
            return False

        if self._r2 != self._c2 and self._r1 == self._c1:
            return True

        return False

    def moveUp(self):
        # vertical
        if self.isUpright:
            self._r1 += 2
            self._c1 += 1

        # flat and wide
        elif self.isWide:
            self._c1 += 1
            self._r1 += 1

        # flat and long
        else:
            self._r1 += 1
            self._c1 += 2

    def moveDown(self):
        # vertical
        if self.isUpright:
            self._r1 -= 1
            self._c1 -= 2

        # flat and wide
        elif self.isWide:
            self._r1 -= 1
            self._c1 -= 1

        # flat and long
        else:
            self._r1 -= 2
            self._c1 -= 1

    # edited
    def moveRight(self):
        # vertical
        if self.isUpright:
            self._r2 += 2
            self._c2 += 1

        # flat and wide
        elif self.isWide:
            self._r2 += 2
            self._c2 += 1

        # flat and long
        else:
            self._r2 += 1
            self._c2 += 1

    # edited
    def moveLeft(self):
        # vertical
        if self.isUpright:
            self._r2 -= 2
            self._c2 -= 1

        # flat and wide
        elif self.isWide:
            self._r2 -= 1
            self._c2 -= 2

        # flat and long
        else:
            self._c2 -= 1
            self._r2 -= 1
