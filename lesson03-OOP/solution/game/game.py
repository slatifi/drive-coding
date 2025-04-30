import pygame
import sys
from player import Player

class Game:
    def __init__(self, WINDOW_SIZE):
        pygame.init()
        self.__screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption("Grid Movement")
        self.__clock = pygame.time.Clock()
        self.__player = Player(0, 0)

    def draw_grid(self, WINDOW_SIZE, CELL_SIZE):
        for x in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.line(self.__screen, (200, 200, 200), (x, 0), (x, WINDOW_SIZE))
        for y in range(0, WINDOW_SIZE, CELL_SIZE):
            pygame.draw.line(self.__screen, (200, 200, 200), (0, y), (WINDOW_SIZE, y))

    def run(self, FPS, WINDOW_SIZE, CELL_SIZE, GRID_SIZE):
        while True:
            self.__clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.__player.move(-1, 0, GRID_SIZE)
                    if event.key == pygame.K_RIGHT:
                        self.__player.move(1, 0, GRID_SIZE)
                    if event.key == pygame.K_UP:
                        self.__player.move(0, -1, GRID_SIZE)
                    if event.key == pygame.K_DOWN:
                        self.__player.move(0, 1, GRID_SIZE)

            self.__screen.fill((255, 255, 255)) # white background
            self.draw_grid(WINDOW_SIZE, CELL_SIZE)
            self.__player.draw(self.__screen, CELL_SIZE)
            pygame.display.flip()