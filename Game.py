class Game:
    def __init__(self):
        self.score = 0
        self.player = None
        self.opponent = None
        self.is_running = False

    def start(self):
        self.is_running = True
        self.score = 0
        print("Game started!")

    def update(self):
        if self.is_running:
            print("Game is updating...")
            # Add game logic here
        else:
            print("Game is not running.")

    def end_game(self):
        self.is_running = False
        print("Game over!")
        print(f"Final score: {self.score}")
        self.reset_game()
        print("Game reset!")


    def reset_game(self):

        self.score = 0
        self.player = None
        self.opponent = None
        print("Game reset!")

    def __str__(self):
        return f"Game(score={self.score}, is_running={self.is_running})"
    def __repr__(self):
        return f"Game(score={self.score}, is_running={self.is_running})"
    def __eq__(self, other):
        if not isinstance(other, Game):
            return False
        return (self.score == other.score and
                self.is_running == other.is_running)
    def __ne__(self, other):
        if not isinstance(other, Game):
            return True
        return (self.score != other.score or
                self.is_running != other.is_running)
    def __lt__(self, other):

        if not isinstance(other, Game):
            return NotImplemented
        return self.score < other.score
    def __le__(self, other):
        if not isinstance(other, Game):
            return NotImplemented
        return self.score <= other.score
    




    
    def convert_enemy_to_star(self):
        if self.is_running:
            self.score += 1
            print(f"Enemy converted to star! Current score: {self.score}")
        else:
            print("Game is not running. Cannot convert enemy.")