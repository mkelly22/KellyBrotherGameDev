"""
Creates MapObject from Tiled string.
"""

import xml.etree.ElementTree as ET
import MapObject

class MapObjectFactory:
    """
    Creates MapObject from Tiled string.
    """

    @staticmethod
    def create(object_string):
        """
        Creates MapObject from Tiled string.
        """
        object_root = ET.fromstring(object_string)
        object_properties = object_root.find('properties')
        map_exit = None
        start_zone = False
        movement = MapObject.EnMovementProperty.NONE
        blocked = False
        for map_property in object_properties:
            if map_property.attrib['name'] == 'exit':
                map_exit = map_property.attrib['value']
            elif map_property.attrib['name'] == 'movement':
                if map_property.attrib['value'] == 'slowed':
                    movement = MapObject.EnMovementProperty.SLOWED
                else:
                    raise Exception("Unsupported movement type" + object_string)
            elif map_property.attrib['name'] == 'blocked':
                if map_property.attrib['type'] != 'bool':
                    raise Exception("Incorrect start_zone type" + object_string)
                if map_property.attrib['value'] == 'true':
                    blocked = True
            elif map_property.attrib['name'] == 'start_zone':
                if map_property.attrib['type'] != 'bool':
                    raise Exception("Incorrect start_zone type" + object_string)
                if map_property.attrib['value'] == 'true':
                    start_zone = True
        return MapObject.MapObject(blocked, movement, start_zone, map_exit)
