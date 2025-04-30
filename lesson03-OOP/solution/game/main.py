from game import Game

# --- Settings ---
WINDOW_SIZE = 400
GRID_SIZE = 8  # 8x8 grid
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 60

if __name__ == "__main__":
    Game(WINDOW_SIZE).run(FPS, WINDOW_SIZE, CELL_SIZE, GRID_SIZE)