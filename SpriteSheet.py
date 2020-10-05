"""
Class to pull individual sprites from sprite sheets.
"""

import pygame


class SpriteSheet:
    """" Class used to grab images out of a spirit sheet. """

    CENTER_HANDLE = 4

    def __init__(self, file_name, cols, rows):
        """"
        Constructor. Pass in the file name of the spirit sheet, group orientation tuple, and character
        orientation tuple. Group orientation is (num groups in x, num groups in y) and character orientation
        is (number of sprites per group in x, numbers of sprites per group in y).
        """

        # Load the spirit sheet.
        self.sheet = pygame.image.load(file_name).convert_alpha()

        self.cols = cols
        self.rows = rows
        self.total_cell_count = cols * rows
        self.rect = self.sheet.get_rect()

        w = self.cell_width = self.rect.width / cols
        h = self.cell_height = self.rect.height / rows

        hw, hh = self.cell_center = (int(w / 2), int(h / 2))

        self.cells = list(
            [(int(index % cols * w), int(int(index / cols) * h), int(w), int(h)) for index in
             range(self.total_cell_count)])
        self.handles = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),
        ])

    def draw(self, surface, cell_index, x, y, handle=0):
        surface.blit(self.sheet, (int(x + self.handles[handle][0]),
                                  int(y + self.handles[handle][1])),
                     self.cells[cell_index])
