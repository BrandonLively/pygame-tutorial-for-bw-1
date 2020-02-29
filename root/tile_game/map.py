from root.tile_game.room import Room


class Map:
    def __init__(self, rooms=Room()):
        self.rooms = rooms
