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
        """Main game loop that handles game execution, event processing, and rendering

        Args:
            FPS: Integer that controls the frame rate of the game
            WINDOW_SIZE: Integer representing the pixel dimensions of the game window
            CELL_SIZE: Integer defining the size of each grid cell in pixels
            GRID_SIZE: Integer representing the number of cells in each dimension of the grid
        """
        while True:
            self.__clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # TO-DO: Complete the following code so the player can move in the grid
                # The player can only move 1 square each time
                # Hint: self.__player.move(x, y, GRID_SIZE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        # make the player to move left 
                        pass
                    if event.key == pygame.K_RIGHT:
                        # make the player to move right
                        pass                       
                    if event.key == pygame.K_UP:
                        # make the player to move up
                        pass
                    if event.key == pygame.K_DOWN:
                        # make the player to move down
                        pass

            self.__screen.fill((255, 255, 255)) # white background
            self.draw_grid(WINDOW_SIZE, CELL_SIZE)
            self.__player.draw(self.__screen, CELL_SIZE)
            pygame.display.flip()