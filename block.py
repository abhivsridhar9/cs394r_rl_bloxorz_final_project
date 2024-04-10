import numpy as np


class Block:

    def __init__(self, r1, c1, r2, c2):
        self._r1 = r1
        self._r2 = r2
        self._c1 = c1
        self._c2 = c2

    def set_coords(self, r1, c1, r2, c2):
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
        return self._r1, self._c1, self._r2, self._c2

    def isUpright(self):
        return self._r1 == self._r2 and self._c1 == self._c2

    def isWide(self):
        return self._r1 == self._r2 and self._c1 != self._c2

        return False

    def move_up(self):
        # vertical
        if self.isUpright():
            self._r1 -= 1
            self._r2 -= 2

        # flat and wide
        elif self.isWide():
            self._r1 -= 1
            self._r2 -= 1

        # flat and long
        else:
            min_r = min(self._r1, self._r2)
            self._r1 = min_r - 1
            self._r2 = min_r - 1

    def move_down(self):
        # vertical
        if self.isUpright():
            self._r1 += 1
            self._r2 += 2

        # flat and wide
        elif self.isWide():
            self._r1 += 1
            self._r2 += 1

        # flat and long
        else:
            max_r = max(self._r1, self._r2)
            self._r1 = max_r + 1
            self._r2 = max_r + 1

    # edited
    def move_right(self):
        # vertical
        if self.isUpright():
            self._c1 += 1
            self._c2 += 2

        # flat and wide
        elif self.isWide():
            max_c = max(self._c1, self._c2)
            self._c1 = max_c + 1
            self._c2 = max_c + 1

        # flat and long
        else:
            self._c1 += 1
            self._c2 += 1

    # edited
    def move_left(self):
        # vertical
        if self.isUpright():
            self._c1 -= 1
            self._c2 -= 2

        # flat and wide
        elif self.isWide():
            min_c = min(self._c1, self._c2)
            self._c1 = min_c - 1
            self._c2 = min_c - 1

        # flat and long
        else:
            self._c1 -= 1
            self._c2 -= 1
