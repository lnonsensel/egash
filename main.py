import cv2
import numpy as np
import config as cfg
from player import draw_player, PlayerState
from grid import draw_grid, get_grid, draw_grid_box, GridState
from ball import draw_ball, BallState
import time
from dataclasses import dataclass
import copy
from utils import put_text

@dataclass
class GameState:
    img: np.ndarray
    grid_state: GridState
    player_state: PlayerState
    ball_state: BallState
    game_over: bool
    player_won: bool

def process_game_end(game_state: GameState, img):
    if game_state.game_over:
        game_state.player_state.moving = False
        game_state.ball_state.vel = 0
        if game_state.player_won:
            put_text(img, 'You win!', (0, 255, 0), 1, 2)
        else:
            put_text(img, 'You lost!', (0, 0, 255), 1, 2)

def init_game():

    width = cfg.WINDOW_WIDTH
    height = cfg.WINDOW_HEIGHT
    img = np.zeros((height, width, 3), dtype=np.uint8)

    grid_state = get_grid()
    ball_state = BallState()
    player_state = PlayerState()

    game_state = GameState(img, grid_state, player_state, ball_state, False, False)

    return game_state

def process_game(game_state):

    width = cfg.WINDOW_WIDTH
    height = cfg.WINDOW_HEIGHT
    grid_state, player_state, ball_state = game_state.grid_state, game_state.player_state, copy.copy(game_state.ball_state)
    img = np.zeros((height, width, 3), dtype=np.uint8)
    game_state.img = img 
    draw_grid(img, grid_state)
    draw_grid_box(img=img)

    player_state = draw_player(img, state=player_state)
    ball_state, grid_state = draw_ball(img = img, state=ball_state, player_state = player_state, grid_state = grid_state)
    time.sleep(0.01)
    if ball_state.ball_fall:
        ball_state.vel = 0
        game_state.game_over = True
        game_state.player_won = False

    elif not np.any(grid_state.grid):
        game_state.game_over = True
        game_state.player_won = True

    process_game_end(game_state, img)
    cv2.imshow('Game', img)
    next_game_state = GameState(img, grid_state, player_state, ball_state, game_state.game_over, game_state.player_won)
    return next_game_state

game_state = init_game()
while True:
    if not game_state.game_over:
        game_state = process_game(game_state)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'): # quit
        break
    
    elif key == ord('r'): # restart
        init_game() 

    elif key == 81: # left arrow
        game_state.player_state.moving = True
        game_state.player_state.moving_right = False
    
    elif key == 83:  # right arrow
        game_state.player_state.moving = True
        game_state.player_state.moving_right = True

    else:
        game_state.player_state.moving = False

cv2.destroyAllWindows()
