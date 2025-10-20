import config as cfg
import cv2
from cv2.typing import MatLike

def draw_player(img: MatLike, bias: int = 0):
    player_pos_y = cfg.WINDOW_HEIGHT - cfg.PLAYER_POS - cfg.PLAYER_HEIGHT

    if bias <= 0:
        bias = 0
    elif bias + cfg.PLAYER_WIDTH >= cfg.WINDOW_WIDTH:
        bias = cfg.WINDOW_WIDTH - cfg.PLAYER_WIDTH

    player_pos_x = bias
    pt1 = (player_pos_x, player_pos_y)
    pt2 = (player_pos_x + cfg.PLAYER_WIDTH, player_pos_y + cfg.PLAYER_HEIGHT)

    cv2.rectangle(img, pt1, pt2, color=[0,0,255], thickness=-1)
    return bias
