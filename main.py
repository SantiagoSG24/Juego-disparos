from Entity import Entity
#         return self.x != 0 or self.y != 0 or self.image is not None
from Character import Character     
from Opponent import Opponent
from Game import Game
if __name__ == "__main__":
    game = Game()
    game.start()
    game.update()
    game.end_game()
    print(game)  # Output: Game(score=0, is_running=False)
    game.reset_game()