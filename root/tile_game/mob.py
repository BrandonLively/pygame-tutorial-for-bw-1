from root.tile_game.entity import Entity


class Mob(Entity):
    def __init__(self, image, rect, room):
        super().__init__(image, rect, room)
