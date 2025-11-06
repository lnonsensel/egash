import config as cfg
import cv2
from cv2.typing import MatLike
from dataclasses import dataclass

@dataclass
class PlayerState:
    bias: int = 0
    y: int = cfg.WINDOW_HEIGHT - cfg.PLAYER_POS - cfg.PLAYER_HEIGHT
    moving: bool = False
    moving_right: bool = False

def draw_player(img: MatLike, state: PlayerState | None = None):
    
    if state is None:
        state = PlayerState()
    state = process_player(state)
    pt1 = (state.bias, state.y)
    pt2 = (state.bias + cfg.PLAYER_WIDTH, state.y+ cfg.PLAYER_HEIGHT)

    cv2.rectangle(img, pt1, pt2, color=[0,0,255], thickness=-1)
    return state

def process_player(state: PlayerState):

    if state.moving:
        if state.moving_right:
            state.bias += cfg.PLAYER_SPEED
        else:
            state.bias -= cfg.PLAYER_SPEED

    if state.bias <= 0:
        state.bias = 0
    elif state.bias + cfg.PLAYER_WIDTH >= cfg.WINDOW_WIDTH:
        state.bias = cfg.WINDOW_WIDTH - cfg.PLAYER_WIDTH

    return state
