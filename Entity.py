class Entity:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def move(self, dx, dy):
        """Move the entity by dx and dy."""
        self.x += dx
        self.y += dy

    def draw(self, screen):
        """Draw the entity on the given screen."""
        screen.blit(self.image, (self.x, self.y))