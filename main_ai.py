import arcade
from snake import Snake
from food import Apple
import pandas as pd
import numpy as np
from keras.models import load_model


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=512, height=512, title='Super Snake')
        arcade.set_background_color(arcade.color.KHAKI)

        self.snake = Snake(self)
        self.food = Apple(self)
        self.score = 0

        self.model = load_model('Output\Snake_Model.h5')

    def on_draw(self):
        arcade.start_render()

        self.snake.draw()
        self.food.draw()

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, 14)
        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        data = {
            'wall_up': self.height - self.snake.center_y,
            'wall_right': self.width - self.snake.center_x,
            'wall_down': self.snake.center_y,
            'wall_left': self.snake.center_x,
            'apple_up': int(self.snake.center_y < self.food.center_y),
            'apple_right': int(self.snake.center_x < self.food.center_x),
            'apple_down': int(self.snake.center_y > self.food.center_y),
            'apple_left': int(self.snake.center_x > self.food.center_x),
            'distance_x': self.snake.center_x - self.food.center_x,
            'distance_y': self.snake.center_y - self.food.center_y
        }

        data_df = pd.DataFrame([data])

        output = self.model.predict(data_df)
        prediction = np.argmax(output)

        if prediction == UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif prediction == RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif prediction == DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif prediction == LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        self.snake.on_update()
        self.food.on_update()

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat_apple(self.food)
            self.score += 1
            self.food = Apple(self)  

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()  
            arcade.exit() 

if __name__ == "__main__":
    # Run the game
    game = Game()
    arcade.run()
