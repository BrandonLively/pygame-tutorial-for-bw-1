class Room:
    def __init__(self, tile_map=None, n_to=None, s_to=None, e_to=None, w_to=None, items=None, entities=None):
        self.tile_map = tile_map
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items
        self.entities = entities
