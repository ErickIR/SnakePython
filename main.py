"#! /usr/bin/env python3" 
import pygame
from pygame.locals import *
from game import Game
import os

COLORS = {
    "BLACK": (  0,   0,   0),
    "WHITE": (255, 255, 255),
    "CIAN":  (  0, 160, 227)
}

pygame.init()
pygame.font.init()

WIDTH = 600
HEIGHT = 600

display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont(None, 96)
clock = pygame.time.Clock()
SCALE = 20


def is_exit_pressed(event):
    return event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.key == pygame.K_ESCAPE or 
                event.key == pygame.K_q
            )
        )


def is_upkey_pressed(event):
    return event.type == pygame.KEYDOWN and (
        event.key == pygame.K_UP or
        event.key == pygame.K_w
    )

def is_downkey_pressed(event):
    return event.type == pygame.KEYDOWN and (
        event.key == pygame.K_DOWN or
        event.key == pygame.K_s
    )

def is_rightkey_pressed(event):
    return event.type == pygame.KEYDOWN and (
        event.key == pygame.K_RIGHT or
        event.key == pygame.K_d
    )

def is_leftkey_pressed(event):
    return event.type == pygame.KEYDOWN and (
        event.key == pygame.K_LEFT or
        event.key == pygame.K_a
    )

def is_pause_pressed(event):
    return event.type == pygame.KEYDOWN and \
        event.key == pygame.K_SPACE

def is_game_restarted(event):
    return event.type == pygame.KEYDOWN and \
        event.key == pygame.K_r

def display_text(message):
    text = font.render(message, True, COLORS["WHITE"])
    display.blit(text, (110, 220))

def main():
    game = Game(SCALE, WIDTH, HEIGHT)
    while True:
        display.fill(COLORS["BLACK"])
        for event in pygame.event.get():
            if is_exit_pressed(event):
                pygame.quit()
            if is_upkey_pressed(event):
                game.set_snake_direction(0, -SCALE)
            if is_downkey_pressed(event):
                game.set_snake_direction(0, SCALE)
            if is_rightkey_pressed(event):
                game.set_snake_direction(SCALE, 0)
            if is_leftkey_pressed(event):
                game.set_snake_direction(-SCALE, 0)
            if is_pause_pressed(event):
                if game.is_paused():
                    game.run()
                else:
                    game.pause()
            if is_game_restarted(event):
                game = Game(SCALE, WIDTH, HEIGHT)
                os.system('cls')
        else: 
            if game.is_running():
                game.update()
                game.show(display, pygame)
            if game.is_paused():
                display_text('PAUSE')
            if game.is_game_over():
                display_text('GAME OVER')
        pygame.display.update()
        clock.tick(game.speed)

if __name__ == "__main__":
    main()

