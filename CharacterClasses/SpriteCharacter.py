from CharacterClasses import SpriteSheet

SPRITE_CHARACTER_DOWN = 0
SPRITE_CHARACTER_LEFT = 1
SPRITE_CHARACTER_RIGHT = 2
SPRITE_CHARACTER_UP = 3


class SpriteCharacter(object):

    def __init__(self, sprite_sheet_dict):
        self.sprite_cols = sprite_sheet_dict['sprite_cols']
        self.sprite_rows = sprite_sheet_dict['sprite_rows']
        self.character_cols = sprite_sheet_dict['character_cols']
        self.character_rows = sprite_sheet_dict['character_rows']

        self.sprite_sheet = SpriteSheet.SpriteSheet(sprite_sheet_dict['file_name'],
                                                    self.sprite_cols * self.character_cols,
                                                    self.sprite_rows * self.character_rows)

        self.direction = SPRITE_CHARACTER_DOWN
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

    def draw_character(self, surface, pos,
                       handle=SpriteSheet.CENTER_CENTER_HANDLE):
        x = pos[0]
        y = pos[1]
        sprite_index = (self.direction * self.sprite_cols * self.character_cols) + self.cur_sprite \
            + ((self.character % self.character_cols) * self.sprite_cols)
        if int(self.character / self.character_cols) == 1:
            sprite_index = sprite_index + (self.character_cols * self.sprite_cols * self.sprite_rows)
        self.sprite_sheet.draw(surface, sprite_index, x, y, handle)

    def next_sprite(self):
        self.cur_sprite = (self.cur_sprite + 1) % self.sprite_cols

    def get_sprite_size_rect(self):
        return self.sprite_sheet.get_sprite_size_rec()
