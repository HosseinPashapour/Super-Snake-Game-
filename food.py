from random import randint
import arcade

class Pear(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Input\Pear.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Apple(arcade.Sprite):
    def __init__(self,game):
        super().__init__("Input\Apple.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Poo(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Input\Poo.png")
        self.width = 36
        self.height = 36
        self.center_x = randint(10,game.width - 10)
        self.center_y = randint(10,game.height - 10)
        self.change_x = 0
        self.change_y = 0
