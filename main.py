import cv2
import numpy as np
import config as cfg
from player import draw_player
from grid import draw_grid, get_grid
width = cfg.WINDOW_WIDTH
height = cfg.WINDOW_HEIGHT

img = np.zeros((height, width, 3), dtype=np.uint8)
grid, points = get_grid()

bias = 0
while True:
    cv2.imshow('Game', img)
    img = np.zeros((height, width, 3), dtype=np.uint8)
    draw_grid(img, grid)
    bias = draw_player(img, bias=bias)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'): # quit
        break
    
    elif key == ord('r'): # restart
        pass 

    elif key == 81: # left arrow
        bias -= cfg.PLAYER_SPEED
    
    elif key == 83:  # right arrow
        bias += cfg.PLAYER_SPEED

cv2.destroyAllWindows()