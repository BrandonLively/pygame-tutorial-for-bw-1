from root.tile_game.item import Item


class Consumable(Item):
    def __init__(self, image, rect, name, healing=0, move_speed_boost=0, atk_speed_boost=0):
        super().__init__(image, rect, name)
        self.healing = healing
        self.move_speed_boost = move_speed_boost
        self.atk_speed_boost = atk_speed_boost
