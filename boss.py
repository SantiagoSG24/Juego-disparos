from Opponent import Opponent

class FinalBoss(Opponent):
    def __init__(self, x, y, speed):
        # Llama al constructor de la clase base Opponent
        super().__init__(x, y, speed * 2)  # El jefe final se mueve el doble de rápido

    def special_attack(self):
        # Método para un ataque especial del jefe final
        print("El jefe final lanza un ataque especial!")


    def move(self):
        # Implementa la lógica de movimiento del jefe final
        # Por ejemplo, moverse en un patrón específico
        pass

        
    def shoot(self):
        # Implementa la lógica de disparo del jefe final
        # Por ejemplo, disparar múltiples proyectiles
        pass

    def draw(self, screen):
        # Implementa la lógica de dibujo del jefe final
        # Por ejemplo, dibujar una imagen diferente para el jefe final
        pass


    def respawn(self, x, y):    
        """
        Respawns the final boss at the given coordinates.
        """
        self.x = x
        self.y = y
        self.lives = 5
        self.is_alive = True
        # Reset other attributes if needed

        self.is_star = False
        # Reset other attributes if needed
        # Reset other attributes if needed