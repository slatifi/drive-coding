import pygame

class Player:
    # constructor
    def __init__(self, pos_x, pos_y, color=(0, 255, 0)):
        # private attributes of player
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__color = color

    # methods of player
    def move(self, dx, dy, GRID_SIZE):
        # Stay inside the grid
        new_x = self.__pos_x + dx
        new_y = self.__pos_y + dy
        if 0 <= new_x < GRID_SIZE and 0 <= new_y < GRID_SIZE:
            self.__pos_x = new_x
            self.__pos_y = new_y

    def draw(self, screen, CELL_SIZE):
        rect = pygame.Rect(self.__pos_x * CELL_SIZE, self.__pos_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.__color, rect)