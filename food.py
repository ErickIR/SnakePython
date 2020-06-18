from random import randint

class Food:
    def __init__(self, scale, WIDTH, HEIGHT):
        self.x = randint(0, int((WIDTH - scale)/scale)) * scale
        self.y = randint(0, int((HEIGHT - scale)/scale)) * scale
        self.scale = scale
    
    def show(self, pygame, display, color):
        pygame.draw.rect(display, color, (self.x, self.y, self.scale, self.scale))
