from Character import Character
from Shot import Shot
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

    
    def respawn(self, x, y):
        """Respawn the entity at the given coordinates."""
        self.x = x
        self.y = y
        # Reset other attributes if needed


    def update(self):

        """Update the entity's state."""
        # Implement update logic here
        pass
    def __str__(self):
        return f"Entity(x={self.x}, y={self.y})"
    def __repr__(self):
        return f"Entity(x={self.x}, y={self.y})"
    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return (self.x == other.x and
                self.y == other.y and
                self.image == other.image)
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        return (self.x, self.y) < (other.x, other.y)
    def __le__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        return (self.x, self.y) <= (other.x, other.y)
    def __gt__(self, other):

        if not isinstance(other, Entity):
            return NotImplemented
        return (self.x, self.y) > (other.x, other.y)
    def __ge__(self, other):
        if not isinstance(other, Entity):
            return NotImplemented
        return (self.x, self.y) >= (other.x, other.y)
    def __hash__(self):
        return hash((self.x, self.y, self.image))
    def __bool__(self):
        return self.x != 0 or self.y != 0 or self.image is not None
    def __len__(self):
        return len(self.image) if self.image else 0
    def __contains__(self, item):
        return item in self.image if self.image else False
    def __getitem__(self, key):
        return self.image[key] if self.image else None
    def __setitem__(self, key, value):
        if self.image is not None:
            self.image[key] = value
        else:
            raise ValueError("Image is None, cannot set item.")
    def __delitem__(self, key):
        if self.image is not None:
            del self.image[key]
        else:
            raise ValueError("Image is None, cannot delete item.")  