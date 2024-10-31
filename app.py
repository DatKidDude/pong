import pygame, sys
         
pygame.init()

class GameBoard:
    """An outline of the playable game area"""
    def __init__(self, screen, color):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.color = color
        self.offset = 25
        # Board surface 
        self.board_surface = pygame.Surface([850, 550])
        self.board_surface_rect = self.board_surface.get_rect()
        self.board_surface_rect.topleft = (self.offset, self.offset)
        # self.board_surface.fill(self.color)
        # Playable game area 
        self.board_rect = pygame.Rect(0, 0, 850, 550)
        pygame.draw.rect(self.board_surface, self.color, self.board_rect, 1, 10)

        # Board center line
        self.center_line = pygame.draw.line(self.board_surface, self.color, (self.board_surface_rect.width / 2, 0), (self.board_surface_rect.width / 2, self.board_surface_rect.height))
    

    def render_board(self):
        """Draw the gameboard"""
        screen.blit(self.board_surface, self.board_surface_rect)

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Create the gameboard
gameboard = GameBoard(screen, WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    gameboard.render_board()

    # Draw everything on the screen
    pygame.display.flip()

    # Limit FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()
