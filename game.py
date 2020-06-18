from snake import Snake
from food import Food

COLORS = {
    "BLACK": (  0,   0,   0),
    "WHITE": (255, 255, 255),
    "CIAN":  (  0, 160, 227)
}

GAME_STATE = {
    'PAUSED': 0,
    'RUNNING': 1,
    'GAME OVER': 3
}

class Game:
    def __init__(self, scale, width, height):
        self.snake = Snake(scale)
        self.food = Food(scale, width, height)
        self.scale = scale
        self.speed = 15
        self.width = width
        self.height = height
        self.score = 0
        self.state = GAME_STATE['RUNNING']
    
    def set_snake_direction(self, x, y):
        self.snake.change_direction(x, y)

    def update(self):
        self.snake.update()
        if self.snake.is_dead(self.width, self.height):
            self.state = GAME_STATE['GAME OVER']
        if self.snake.can_eat(self.food):
            self.snake.eat(self.food)
            self.food = Food(self.scale, WIDTH=self.width, HEIGHT=self.height)
            self.score += 1
    
    def show(self, display, pygame):
        self.snake.show(pygame, display, COLORS["WHITE"])
        self.food.show(pygame, display, COLORS["CIAN"])

    def is_paused(self):
        return self.state == GAME_STATE['PAUSED']

    def pause(self):
        self.state = GAME_STATE['PAUSED']
    
    def run(self):
        self.state = GAME_STATE['RUNNING']
    
    def game_over(self):
        self.state = GAME_STATE['GAME OVER']
    
    def is_game_over(self):
        return self.state == GAME_STATE['GAME OVER']
    
    def is_running(self):
        return self.state == GAME_STATE['RUNNING']
