from CharacterClasses.SpriteCharacter import *
from CharacterClasses.MovingCharacter import *

DEFAULT_SPEED = 2  # pixels / frame
DEFAULT_UPDATE_RATE = 15  # 1 update / X FPS


class PlayerCharacter(SpriteCharacter, MovingCharacter):

    def __init__(self, pos, map_size, sprite_sheet_dict, speed=DEFAULT_SPEED, sprite_update_rate=DEFAULT_UPDATE_RATE):
        SpriteCharacter.__init__(self, sprite_sheet_dict)
        MovingCharacter.__init__(self, (self.sprite_sheet.cell_width, self.sprite_sheet.cell_height), pos, speed)
        self.map_size = map_size
        self.direction = SPRITE_CHARACTER_DOWN
        self.sprite_update_rate = sprite_update_rate
        self.frame_count = 0

    def move(self, move_left, move_right, move_up, move_down):
        self.moving = False
        self.prev_pos[0] = self.pos[0]
        self.prev_pos[1] = self.pos[1]
        direction = SPRITE_CHARACTER_UP
        if move_up:
            self.pos[1] = self.pos[1] - self.speed
            self.moving = True
        if move_down:
            self.pos[1] = self.pos[1] + self.speed
            self.moving = True
            direction = SPRITE_CHARACTER_DOWN
        if move_left:
            self.pos[0] = self.pos[0] - self.speed
            self.moving = True
            direction = SPRITE_CHARACTER_LEFT
        if move_right:
            self.pos[0] = self.pos[0] + self.speed
            self.moving = True
            direction = SPRITE_CHARACTER_RIGHT

        if self.moving:
            self.set_direction(direction)
            self.frame_count = self.frame_count + 1
            if self.frame_count >= self.sprite_update_rate:
                self.next_sprite()
                self.frame_count = 0

    def draw_character(self, surface):
        SpriteCharacter.draw_character(self, surface, self.pos)
