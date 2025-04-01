from Character import Character
from boss import FinalBoss
class Opponent(Character):
    def __init__(self, is_star=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_star = is_star

    def move(self):
        # Implement the logic for the opponent's movement
        pass

    def shoot(self):
        # Implement the logic for the opponent's shooting
        pass

    def collide(self, other_entity):
        # Implement the logic for collision with another entity
        if self.lives > 0:
            self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False   


    def draw(self, screen):
        # Implement the logic for drawing the opponent on the screen
        pass    


    def respawn(self, x, y):
        """
        Respawns the opponent at the given coordinates.
        """
        self.x = x
        self.y = y
        self.lives = 3
        self.is_alive = True
        # Reset other attributes if needed
        self.is_star = False
        # Reset other attributes if needed  


    def update(self):
        # Implement the logic for updating the opponent's state
        pass    

    def __str__(self):
        return f"Opponent(lives={self.lives}, is_alive={self.is_alive}, is_star={self.is_star})"
    
    def __repr__(self):
        return f"Opponent(lives={self.lives}, is_alive={self.is_alive}, is_star={self.is_star})"
    

    def __eq__(self, other):
        if not isinstance(other, Opponent):
            return False
        return (self.lives == other.lives and
                self.is_alive == other.is_alive and
                self.is_star == other.is_star)

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __lt__(self, other):


        if not isinstance(other, Opponent):
            return NotImplemented
        return self.lives < other.lives
    
    def __le__(self, other):
        if not isinstance(other, Opponent):
            return NotImplemented
        return self.lives <= other.lives
    
    