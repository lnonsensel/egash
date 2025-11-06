import numpy as np
import config as cfg
import cv2
from dataclasses import dataclass, field
from player import PlayerState
from grid import GridState

@dataclass
class BallState:
    x: int = cfg.WINDOW_WIDTH // 2
    y: int = cfg.WINDOW_HEIGHT - cfg.PLAYER_POS - cfg.PLAYER_HEIGHT - cfg.BALL_R
    vel: int = cfg.INITIAL_VELOCITY
    # vec: list[int, int] = field(default_factory=list)
    vec: list[int, int] = field(default_factory = lambda: cfg.INITIAL_VECTOR)
    ball_fall: bool = False


def draw_ball(img, state: BallState, player_state: PlayerState, grid_state: GridState):
    state, grid_state = process_ball(state, player_state, grid_state)
    pt = (state.x, state.y)
    cv2.circle(img = img, center = pt, radius = cfg.BALL_R, color = (128,0,128), thickness = -1)
    return state, grid_state


def process_ball(state: BallState, player_state: PlayerState, grid_state: GridState):
    state, grid_state = process_collision(state, player_state, grid_state)
    coords = np.asarray([state.x, state.y])
    coords += np.asarray(state.vec) * state.vel
    return BallState(coords[0], coords[1], state.vel, state.vec, state.ball_fall), grid_state

def process_collision(state: BallState, player_state: PlayerState, grid_state: GridState):

    if state.x - cfg.BALL_R < 0 or state.x + cfg.BALL_R > cfg.WINDOW_WIDTH:
        state.vec[0] *= -1
    if state.y - cfg.BALL_R < 0:
        state.vec[1] *= -1
    if state.y + cfg.BALL_R >= player_state.y and player_state.bias <= state.x <= player_state.bias + cfg.PLAYER_WIDTH:
        state.vec[1] *= -1
    if state.y > cfg.WINDOW_HEIGHT:
        state.ball_fall = True
        


    new_coords = []
    new_block_coords = []
    for coord, box_points in zip(grid_state.coords, grid_state.block_coords):
        pt1, pt2 = box_points
        x1, y1 = pt1
        x2, y2 = pt2
        if (y1 + cfg.BALL_R <= state.y <= y2 + cfg.BALL_R and x1 +cfg.BALL_R <= state.x <= x2 + cfg.BALL_R):
            state.vec[1] *= -1 
            state.vel = round(state.vel * cfg.ACCELERATION)
            grid_state.grid[*coord] = 0
        else:
            new_coords.append(coord)
            new_block_coords.append(box_points)

    grid_state.coords = new_coords
    grid_state.block_coords = new_block_coords

    return state, grid_state
