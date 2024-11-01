import pygame
import sys
import random
         
pygame.init()


class Ball:
    """A ball that the paddles hit"""

    def __init__(self, board, color):
        self.board = board
        self.color = color
        # Set the starting position in the center of the board
        self.center = pygame.math.Vector2(
            self.board.center_line.x,
            self.board.center_line.height // 2
            )
        self.speed = pygame.math.Vector2(10, 10)
        self.radius = 10
        # Draw the ball 
        self.ball_obj = pygame.draw.circle(
            self.board.board_surface, self.color, self.center, self.radius
        )


    def update(self):
        """Move the ball around"""
        self.ball_obj.move_ip(self.speed)

        # if self.ball_obj.right >= self.board.board_rect.right or self.ball_obj.left < 0:
        #     self.speed.x = -self.speed.x 
        
        if self.ball_obj.bottom >= self.board.board_rect.bottom or self.ball_obj.top < 0:
            self.speed.y = -self.speed.y
        
        pygame.draw.circle(self.board.board_surface, self.color, self.ball_obj.center, self.radius)

class Paddle:
    """A paddle to hit the ball"""
    def __init__(self, board, color, x, y):
        # Gameboard object
        self.board = board
        self.color = color
        self.x = x
        self.y = y
        self.speed = 20

        # Create the paddle
        self.paddle = pygame.Rect(self.x, self.y, 10, 70)
        # self.paddle_rect = pygame.draw.rect(self.board.board_surface, self.color, self.paddle, 0, 2)
        self.moving = False


    def update(self):
        """Move the paddle"""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] and self.paddle.bottom < self.board.board_rect.bottom:
            self.paddle.move_ip(0, self.speed)
        elif keys[pygame.K_UP] and self.paddle.top > 0:
            self.paddle.move_ip(0, -self.speed)

        pygame.draw.rect(self.board.board_surface, self.color, self.paddle, 0, 2)


class AI(Paddle):
    def __init__(self, board, color, x, y, ball):
        super().__init__(board, color, x, y)
        self.ball = ball

    def update(self):
        """Have the computer follow the ball"""
        self.paddle.bottom = self.ball.ball_obj.bottom 

        pygame.draw.rect(self.board.board_surface, self.color, self.paddle, 0, 2)

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
        # Board outline 
        self.board_rect = pygame.Rect(0, 0, 850, 550)
        # Board center line
        self.center_line = pygame.draw.line(self.board_surface, self.color, (self.board_surface_rect.width / 2, 0), (self.board_surface_rect.width / 2, self.board_surface_rect.height))


    def render_board(self):
        """Draw the gameboard"""
        # Draw the board surface on the screen
        self.screen.blit(self.board_surface, self.board_surface_rect)
        # Update the board surface 
        self.board_surface.fill("black")
        # Draw the board outline
        pygame.draw.rect(self.board_surface, self.color, self.board_rect, 1, 10)
        # Draw the board center line
        pygame.draw.line(self.board_surface, self.color, (self.board_surface_rect.width / 2, 0), (self.board_surface_rect.width / 2, self.board_surface_rect.height))
        

def hit_ball(player, ai_player, ball):
    """Check if player or ai has hit the ball"""
    if player.paddle.colliderect(ball.ball_obj) or ai_player.paddle.colliderect(ball.ball_obj):
        ball.speed.x = -ball.speed.x


SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Create the gameboard
gameboard = GameBoard(screen, WHITE)
# Create the player
ball = Ball(gameboard, "maroon")
player = Paddle(gameboard, GREEN, 10, 0)
ai_player = AI(gameboard, GREEN, 830, 0, ball)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()
    ai_player.update()
    ball.update()
    hit_ball(player, ai_player, ball)
    gameboard.render_board()

    # Draw everything on the screen
    pygame.display.update()

    # Limit FPS
    clock.tick(FPS)

pygame.quit()
sys.exit()

