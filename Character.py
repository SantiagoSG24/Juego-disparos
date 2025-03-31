from Entity import Entity

class Character(Entity):
    def __init__(self, lives):
        super().__init__()
        self.lives = lives
        self.is_alive = True

    def move(self, direction):
        """
        Moves the character in the specified direction.
        :param direction: A string indicating the direction (e.g., 'up', 'down', 'left', 'right').
        """
        # Implement movement logic here
        pass

    def shoot(self):
        """
        Handles the shooting action of the character.
        """
        # Implement shooting logic here
        pass

    def collide(self, other_entity):
        """
        Handles collision with another entity.
        :param other_entity: The entity this character collides with.
        """
        # Implement collision logic here
        if self.lives > 0:
            self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False

    def draw(self, screen):
        """
        Draws the character on the screen.
        :param screen: The screen to draw on.
        """
        # Implement drawing logic here  

        pass
    def respawn(self, x, y):
        """     "
        "Respawns the character at the given coordinates."
        """
        self.x = x
        self.y = y
        self.lives = 3
        self.is_alive = True    

    def update(self):
        """
        Updates the character's state (e.g., position, animation).
        """
        # Implement update logic here
        pass
    def __str__(self):
        return f"Character(lives={self.lives}, is_alive={self.is_alive})"
    def __repr__(self):
        return f"Character(lives={self.lives}, is_alive={self.is_alive})"   
    

if __name__ == "__main__":
    # Example usage
    character = Character(lives=3)
    print(character)  # Output: Character(lives=3, is_alive=True)
    character.move("up")
    character.shoot()
    print(character)  # Output: Character(lives=3, is_alive=True)
    character.collide(Entity(0, 0, None))  # Simulate collision
    print(character)  # Output: Character(lives=2, is_alive=True)   