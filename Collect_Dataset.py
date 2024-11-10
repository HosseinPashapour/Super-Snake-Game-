import arcade
from snake import Snake
from food import Apple
import pandas as pd

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=512, height=512, title='Super Snake')
        arcade.set_background_color(arcade.color.BLACK)

        self.snake = Snake(self)  
        self.apple = Apple(self)    
        self.score = 0           
        self.data = []            

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(f"Score: {self.score}", 10, 10)  
        self.snake.draw()  
        self.apple.draw()  
        arcade.finish_render()

    def on_update(self, delta_time: float):
        if len(self.data) >= 10000:
            df = pd.DataFrame(self.data)
            df.to_csv('Input\Snake_Dataset.csv', index=False)
            arcade.close_window()
            arcade.exit()

        self.snake.move()

        distance_x = self.snake.center_x - self.apple.center_x
        distance_y = self.snake.center_y - self.apple.center_y

        data = {
            'wall_up': self.height - self.snake.center_y,
            'wall_down': self.snake.center_y,
            'wall_left': self.snake.center_x,
            'wall_right': self.width - self.snake.center_x,
            'apple_up': int(self.snake.center_y < self.apple.center_y and abs(distance_x) < self.snake.width),
            'apple_right': int(self.snake.center_x < self.apple.center_x and abs(distance_y) < self.snake.height),
            'apple_down': int(self.snake.center_y > self.apple.center_y and abs(distance_x) < self.snake.width),
            'apple_left': int(self.snake.center_x > self.apple.center_x and abs(distance_y) < self.snake.height),
            'distance_x': distance_x,
            'distance_y': distance_y,
            'direction': None 
        }

        if abs(distance_x) > abs(distance_y):
            if distance_x > 0:
                self.snake.change_x = -1
                self.snake.change_y = 0
                data['direction'] = LEFT
                print("LEFT")
            else:
                self.snake.change_x = 1
                self.snake.change_y = 0
                data['direction'] = RIGHT
                print("RIGHT")
        else:
            if distance_y > 0:
                self.snake.change_x = 0
                self.snake.change_y = -1
                data['direction'] = DOWN
                print("DOWN")
            else:
                self.snake.change_x = 0
                self.snake.change_y = 1
                data['direction'] = UP
                print("UP")

        if all(v is not None for v in data.values()):
            self.data.append(data)

        self.snake.on_update(delta_time)
        self.apple.on_update()

        if arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat_apple(self.apple)
            self.score += 1
            self.apple = Apple(self) 
            print("Apple Eaten")

if __name__ == '__main__':
    game = Game()
    arcade.run()
