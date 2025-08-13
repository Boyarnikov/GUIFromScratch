import random

from .patch import Patch

class ShakingPatch(Patch):
    def update(self):
        self.position = (self.position[0] + random.randint(-5, 5), self.position[1] + random.randint(-5, 5))