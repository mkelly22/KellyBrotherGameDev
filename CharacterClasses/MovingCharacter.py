import math

class MovingCharacter(object):
    def __init__(self, size, pos, speed):
        self.size = size
        self.pos = list(pos)
        self.prev_pos = list(pos)
        self.speed = speed
        self.moving = False

    def is_moving(self):
        return self.moving

    def get_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos

    def get_rect(self):
        return self.rect

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def get_prev_pos(self):
        return self.prev_pos

    def set_prev_pos(self, prev_pos):
        self.prev_pos = prev_pos

    def get_movement_area(self, map_tile_size):
        x_min = self.pos[0] - (self.size[0] / 2)
        x_max = self.prev_pos[0] + (self.size[0] / 2)
        y_min = self.pos[1] - (self.size[1] / 2)
        y_max = self.prev_pos[1] + (self.size[1] / 2)
        if self.prev_pos[0] < self.pos[0]:
            x_min = self.prev_pos[0] - (self.size[0] / 2)
            x_max = self.pos[0] + (self.size[0] / 2)
        if self.prev_pos[1] < self.pos[1]:
            y_min = self.prev_pos[1] - (self.size[1] / 2)
            y_max = self.pos[1] + (self.size[1] / 2)

        if (x_min % map_tile_size[0]) != 0:
            x_min = x_min - (x_min % map_tile_size[0])
        if (x_max % map_tile_size[0]) != 0:
            x_max = x_max + map_tile_size[0] - (x_max % map_tile_size[0])
        if (y_min % map_tile_size[1]) != 0:
            y_min = y_min - (y_min % map_tile_size[1])
        if (y_max % map_tile_size[1]) != 0:
            y_max = y_max + map_tile_size[0] - (y_max % map_tile_size[1])

        width = x_max - x_min
        height = y_max - y_min

        return x_min, y_min, width, height
