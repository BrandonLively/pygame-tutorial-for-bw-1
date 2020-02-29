from root.tile_game.item import Item


class Weapon(Item):
    def __init__(self, image, rect, name, damage, atk_speed):
        super().__init__(image, rect, name)
        self.damage = damage
        self.atk_speed = atk_speed
