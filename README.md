# Juego-disparos
https://github.com/SantiagoSG24/Juego-disparos.git
. Importaciones
python
Copiar
Editar
from Character import Character
from Shot import Shot
Importa Character y Shot, lo que sugiere que Entity es una clase base para personajes (Character) y disparos (Shot), aunque no se usan dentro de esta clase.

2. Constructor (__init__)
python
Copiar
Editar
def __init__(self, x, y, image):
    self.x = x
    self.y = y
    self.image = image
x, y: Representan la posición de la entidad en la pantalla.

image: Contiene la imagen que se usará para representar la entidad en el juego (probablemente una superficie de pygame).

3. Métodos principales
Movimiento
python
Copiar
Editar
def move(self, dx, dy):
    """Move the entity by dx and dy."""
    self.x += dx
    self.y += dy
Mueve la entidad sumando dx y dy a sus coordenadas actuales.

Dibujar en pantalla
python
Copiar
Editar
def draw(self, screen):
    """Draw the entity on the given screen."""
    screen.blit(self.image, (self.x, self.y))
Usa screen.blit() (de pygame) para mostrar la imagen en la pantalla.

Reaparición (respawn)
python
Copiar
Editar
def respawn(self, x, y):
    """Respawn the entity at the given coordinates."""
    self.x = x
    self.y = y
    # Reset other attributes if needed
Reposiciona la entidad en las coordenadas (x, y).

Actualizar (update)
python
Copiar
Editar
def update(self):
    """Update the entity's state."""
    pass
Método vacío que se puede sobrescribir en clases hijas para actualizar el estado de la entidad en cada fotograma.

4. Métodos especiales (dunder methods)
Estos métodos permiten que la clase Entity interactúe con Python de formas específicas.

Conversión a texto (__str__ y __repr__)
python
Copiar
Editar
def __str__(self):
    return f"Entity(x={self.x}, y={self.y})"

def __repr__(self):
    return f"Entity(x={self.x}, y={self.y})"
__str__(): Devuelve un texto legible cuando se usa print(entity).

__repr__(): Devuelve un texto útil para depuración en la consola.

Comparaciones (==, !=, <, <=, >, >=)
Estos métodos permiten comparar objetos Entity.

python
Copiar
Editar
def __eq__(self, other):
    if not isinstance(other, Entity):
        return False
    return (self.x == other.x and self.y == other.y and self.image == other.image)
__eq__(): Dos entidades son iguales si tienen la misma posición (x, y) y la misma imagen.

python
Copiar
Editar
def __ne__(self, other):
    return not self.__eq__(other)
__ne__(): Define != como la negación de ==.

python
Copiar
Editar
def __lt__(self, other):
    if not isinstance(other, Entity):
        return NotImplemented
    return (self.x, self.y) < (other.x, other.y)
__lt__(): Permite comparar entidades con < basándose en x, y.

python
Copiar
Editar
def __le__(self, other):
    if not isinstance(other, Entity):
        return NotImplemented
    return (self.x, self.y) <= (other.x, other.y)
__le__(): Permite usar <=.

python
Copiar
Editar
def __gt__(self, other):
    if not isinstance(other, Entity):
        return NotImplemented
    return (self.x, self.y) > (other.x, other.y)
__gt__(): Permite usar >.

python
Copiar
Editar
def __ge__(self, other):
    if not isinstance(other, Entity):
        return NotImplemented
    return (self.x, self.y) >= (other.x, other.y)
__ge__(): Permite usar >=.

Hash y Booleanos
python
Copiar
Editar
def __hash__(self):
    return hash((self.x, self.y, self.image))
__hash__(): Permite usar Entity como clave en set o dict.

python
Copiar
Editar
def __bool__(self):
    return self.x != 0 or self.y != 0 or self.image is not None
__bool__(): Hace que Entity sea True si tiene posición o imagen.

Manipulación de image como estructura indexable
Estos métodos tratan image como si fuera una lista o diccionario, pero solo funcionan si image es una estructura indexable.

python
Copiar
Editar
def __len__(self):
    return len(self.image) if self.image else 0
__len__(): Devuelve el tamaño de image si existe.

python
Copiar
Editar
def __contains__(self, item):
    return item in self.image if self.image else False
__contains__(): Permite usar in para verificar si algo está en image.

python
Copiar
Editar
def __getitem__(self, key):
    return self.image[key] if self.image else None
__getitem__(): Permite acceder a image[key], como si image fuera una lista/diccionario.

python
Copiar
Editar
def __setitem__(self, key, value):
    if self.image is not None:
        self.image[key] = value
    else:
        raise ValueError("Image is None, cannot set item.")
__setitem__(): Permite modificar image[key].

python
Copiar
Editar
def __delitem__(self, key):
    if self.image is not None:
        del self.image[key]
    else:
        raise ValueError("Image is None, cannot delete item.")
__delitem__(): Permite eliminar elementos de image.

