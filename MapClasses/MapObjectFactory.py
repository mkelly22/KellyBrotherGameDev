import xml.etree.ElementTree as ET


class MapObjectFactory:

    @staticmethod
    def create(object_string):
        object_root = ET.fromstring(object_string)
        object_properties = object_root.find('properties')
        map_exit = None
        start_zone = False
        movement = EnMovementProperty.NONE
        blocked = False
        for map_property in object_properties:
            if map_property.attrib['name'] is 'exit':
                map_exit = map_property.attrib['value']
            elif map_property.attrib['name'] is 'movement':
                if map_property.attrib['value'] is 'slowed':
                    movement = EnMovementProperty.SLOWED
                else:
                    raise Exception("Unsupported movement type" + object_string)
            elif map_property.attrib['name'] is 'blocked':
                if map_property.attrib['type'] is not 'bool':
                    raise Exception("Incorrect start_zone type" + object_string)
                if map_property.attrib['value'] is 'true':
                    blocked = True
            elif map_property.attrib['name'] is 'start_zone':
                if map_property.attrib['type'] is not 'bool':
                    raise Exception("Incorrect start_zone type" + object_string)
                if map_property.attrib['value'] is 'true':
                    start_zone = True
        return MapObject(blocked, movement, start_zone, map_exit)