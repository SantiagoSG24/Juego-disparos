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




            def lose_life(self):
                if self.player and hasattr(self.player, 'lives'):
                    self.player.lives -= 1
                    print(f"Player hit! Lives remaining: {self.player.lives}")
                    if self.player.lives <= 0:
                        print("Player has no lives left!")
                        self.end_game()
                else:
                    print("Player does not have a lives attribute.")
                    

            def increase_score(self, points):
                if self.is_running:
                    self.score += points
                    print(f"Score increased by {points}. Current score: {self.score}")
                else:
                    print("Game is not running. Cannot increase score.")

                    
                    def display_score_and_lives(self):
                        if self.player and hasattr(self.player, 'lives'):
                            print(f"Score: {self.score}, Lives: {self.player.lives}")
                        else:
                            print(f"Score: {self.score}, Lives: N/A")