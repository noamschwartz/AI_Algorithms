class Node:
    def __init__(self, junction):
        self.index = junction.index
        self.links = junction.links
        self.parents = None
        self.lat = junction.lat
        self.lon = junction.lon
