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
        """Moves the player position in the grid
        Args:
            dx: Integer representing horizontal movement (positive for right, negative for left)
            dy: Integer representing vertical movement (positive for down, negative for up)
            GRID_SIZE: Integer defining the dimensions of the square grid to ensure player stays within bounds
        """
        # Complete the move method so the player can move in the grid, make sure the new position is within the grid!
        # Hint: new_x = self.__pos_x + dx



    def draw(self, screen, CELL_SIZE):
        rect = pygame.Rect(self.__pos_x * CELL_SIZE, self.__pos_y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, self.__color, rect)