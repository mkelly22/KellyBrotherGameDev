from enum import Enum


class EnMovementProperty(Enum):
    NONE = 0
    SLOWED = 1


class MapObject:

    def __init__(self, blocked, movement, start_zone, map_exit):
        self.blocked = blocked
        self.movement = movement
        self.start_zone = start_zone
        self.map_exit = map_exit

    def get_exit(self):
        return self.map_exit

    def get_blocked(self):
        return self.blocked

    def get_movement(self):
        return self.movement

    def get_start_zone(self):
        return self.start_zone

    def to_string(self):
        map_object_str = "blocked: " + str(self.blocked) + '\n' + "movement: " + str(
            self.movement) + '\n' + "start_zone: " + str(self.start_zone) + '\n' + "map_exit: " + str(
            self.map_exit) + '\n'
        return map_object_str
