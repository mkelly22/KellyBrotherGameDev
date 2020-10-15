"""
Class to pull individual sprites from sprite sheets.
"""

import pygame

TOP_LEFT_HANDLE = 0
TOP_CENTER_HANDLE = 1
TOP_RIGHT_HANDLE = 2
CENTER_LEFT_HANDLE = 3
CENTER_CENTER_HANDLE = 4
CENTER_RIGHT_HANDLE = 5
BOTTOM_LEFT_HANDLE = 6
BOTTOM_CENTER_HANDLE = 7
BOTTOM_RIGHT_HANDLE = 8


class SpriteSheet:
    """" Class used to grab images out of a spirit sheet. """

    def __init__(self, file_name, cols, rows, convert_alpha=True, pixel_boundary=False):
        """"
        Constructor. Pass in the file name of the spirit sheet, group orientation tuple, and character
        orientation tuple. Group orientation is (num groups in x, num groups in y) and character orientation
        is (number of sprites per group in x, numbers of sprites per group in y).
        """

        # Load the spirit sheet.
        if convert_alpha:
            self.sheet = pygame.image.load(file_name).convert_alpha()
        else:
            self.sheet = pygame.image.load(file_name)

        self.cols = cols
        self.rows = rows
        self.total_cell_count = cols * rows
        self.rect = self.sheet.get_rect()

        if not pixel_boundary:
            w = self.cell_width = self.rect.width / cols
            h = self.cell_height = self.rect.height / rows
        else:
            w = self.cell_width = (self.rect.width - (cols + 1)) / cols
            h = self.cell_height = (self.rect.height - (rows + 1)) / rows

        hw, hh = self.cell_center = (int(w / 2), int(h / 2))

        self.cells = list(
            [[int(index % cols * w), int(int(index / cols) * h), int(w), int(h)] for index in
             range(self.total_cell_count)])

        # adjust for pixel boundary
        if pixel_boundary:
            x_adjust = 1
            y_adjust = 1
            for cell in self.cells:
                cell[0] = cell[0] + x_adjust
                cell[1] = cell[1] + y_adjust
                x_adjust = x_adjust + 1
                if x_adjust == (self.cols + 1):
                    x_adjust = 1
                    y_adjust = y_adjust + 1

        self.handles = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),
        ])

    def draw(self, surface, cell_index, x, y, handle=0):
        surface.blit(self.sheet, (int(x + self.handles[handle][0]),
                                  int(y + self.handles[handle][1])),
                     self.cells[cell_index])

    def get_sprite_size_rec(self):
        return self.cell_width, self.cell_height
