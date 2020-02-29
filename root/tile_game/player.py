from root.tile_game.entity import Entity


class Player(Entity):
    def __init__(self, image, rect, room, inventory=None, equipped_weapon=None):
        super().__init__(image, rect, room)
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon
