from SpriteSheet import *


class SpriteCharacter:
    CHARACTER_DOWN = 0
    CHARACTER_LEFT = 1
    CHARACTER_RIGHT = 2
    CHARACTER_UP = 3

    def __init__(self, file_name, sprite_cols, rows, character_cols, character_rows):
        self.sprite_sheet = SpriteSheet(file_name, sprite_cols * character_cols, rows * character_rows)

        self.sprite_cols = sprite_cols
        self.sprite_rows = rows
        self.character_cols = character_cols
        self.character_rows = character_rows

        self.direction = self.CHARACTER_DOWN
        self.character = 0
        self.cur_sprite = 0

    def set_direction(self, direction):
        if self.direction != direction:
            self.direction = direction
            self.cur_sprite = 0

    def next_character(self):
        self.character = (self.character + 1) % (self.character_cols * self.character_rows)

    def previous_character(self):
        if self.character == 0:
            self.character = (self.character_cols * self.character_rows) - 1
        else:
            self.character = self.character - 1

    def draw_character(self, surface, x, y, handle=SpriteSheet.CENTER_HANDLE):
        sprite_index = (self.direction * self.sprite_cols * self.character_cols) + self.cur_sprite + (
                               (self.character % self.character_cols) * self.sprite_cols)
        if int(self.character / self.character_cols) == 1:
            sprite_index = sprite_index + (self.character_cols * self.sprite_cols * self.sprite_rows)
        self.sprite_sheet.draw(surface, sprite_index, x, y, handle)

    def next_sprite(self):
        self.cur_sprite = (self.cur_sprite + 1) % self.sprite_cols
