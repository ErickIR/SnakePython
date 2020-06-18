from helper import *

class Snake:
    def __init__(self, scale):
        self.x = 200
        self.y = 200
        self.scale = scale
        self.blocks = []
        self.blocks.append((self.x, self.y, self.scale, self.scale))
        self.food_eated = []
        self.total = 0
        self.x_speed = 0
        self.y_speed = 0
    
    def change_direction(self, x, y):
        self.x_speed = x 
        self.y_speed = y

    def can_eat(self, food):
        dist = calculate_distance((self.x, self.y), (food.x, food.y))
        if(dist <= 1.0):
            return True
        return False
    
    def eat(self, food):
        self.food_eated.append(food)
        last = self.blocks[len(self.blocks) - 1]
        new_block = (last[0], last[1] + (self.scale), self.scale, self.scale)
        self.blocks.append(new_block)
        self.total += 1

    def update(self):
        new_block_list = []
        for i in range(1, len(self.blocks)):
            new_block_list.append(self.blocks[i - 1])
        new_x = self.x + self.x_speed 
        new_y = self.y + self.y_speed 
        self.x = new_x 
        self.y = new_y
        new_head = (self.x, self.y, self.scale, self.scale)
        new_block_list.insert(0, new_head)
        self.blocks = new_block_list

    def show(self, pygame, display, color):
        for block in self.blocks:
            pygame.draw.rect(display, color, block)
            
    
    
    def is_dead(self, WIDTH, HEIGHT):
        return is_wall_colliding((self.x, self.y), WIDTH, HEIGHT) or is_snake_colliding(self.blocks)

    