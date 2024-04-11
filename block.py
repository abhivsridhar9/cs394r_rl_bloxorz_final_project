import numpy as np


class Block:

    def __init__(self, r1, c1, r2, c2):
        self._r1 = r1
        self._r2 = r2
        self._c1 = c1
        self._c2 = c2

        self._focus_block = 0

    def set_coords(self, r1, c1, r2, c2):
        self._r1 = r1
        self._r2 = r2
        self._c1 = c1
        self._c2 = c2

    def get_coords(self):
        return self._r1, self._c1, self._r2, self._c2

    def is_upright(self):
        return self._r1 == self._r2 and self._c1 == self._c2

    def is_wide(self):
        return self._r1 == self._r2 and self._c1 != self._c2

    def move_up(self):
        match self._focus_block:
            case 0:
                # vertical
                if self.is_upright():
                    self._r1 -= 1
                    self._r2 -= 2

                # flat and wide
                elif self.is_wide():
                    self._r1 -= 1
                    self._r2 -= 1

                # flat and long
                else:
                    min_r = min(self._r1, self._r2)
                    self._r1 = min_r - 1
                    self._r2 = min_r - 1

            case 1:
                self._r1 -= 1

            case 2:
                self._r2 -= 1

    def move_down(self):
        match self._focus_block:
            case 0:
                # vertical
                if self.is_upright():
                    self._r1 += 1
                    self._r2 += 2

                # flat and wide
                elif self.is_wide():
                    self._r1 += 1
                    self._r2 += 1

                # flat and long
                else:
                    max_r = max(self._r1, self._r2)
                    self._r1 = max_r + 1
                    self._r2 = max_r + 1

            case 1:
                self._r1 += 1
            case 2:
                self._r2 += 1

    # edited
    def move_right(self):
        match self._focus_block:
            case 0:
                # vertical
                if self.is_upright():
                    self._c1 += 1
                    self._c2 += 2

                # flat and wide
                elif self.is_wide():
                    max_c = max(self._c1, self._c2)
                    self._c1 = max_c + 1
                    self._c2 = max_c + 1

                # flat and long
                else:
                    self._c1 += 1
                    self._c2 += 1

            case 1:
                self._c1 += 1
            case 2:
                self._c2 += 1

    # edited
    def move_left(self):
        match self._focus_block:
            case 0:
                # vertical
                if self.is_upright():
                    self._c1 -= 1
                    self._c2 -= 2

                # flat and wide
                elif self.is_wide():
                    min_c = min(self._c1, self._c2)
                    self._c1 = min_c - 1
                    self._c2 = min_c - 1

                # flat and long
                else:
                    self._c1 -= 1
                    self._c2 -= 1
            case 1:
                self._c1 -= 1
            case 2:
                self._c2 -= 1

    def set_focus_block(self, focus_block=1):
        if focus_block == 0:
            self._focus_block = 0
        elif self._focus_block == 1:
            self._focus_block = 2
        else:
            self._focus_block = 1

    def get_focus(self):
        return self._focus_block

    def join_single_blocks(self):
        if self._focus_block == 1 or self._focus_block == 2:
            if abs(self._r1 - self._r2) == 1 and (self._c1 == self._c2):
                self.set_focus_block(0)
            elif abs(self._c1 - self._c2) == 1 and (self._r1 == self._r2):
                self.set_focus_block(0)
