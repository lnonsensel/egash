import numpy as np
import config as cfg
import cv2

import random

def get_grid():
    right_border_w = cfg.WINDOW_WIDTH - cfg.GRID_BIAS_X
    left_border_w = cfg.GRID_BIAS_X
    num_blocks_width = (right_border_w - left_border_w) // cfg.BLOCK_WIDTH

    top_border_h = cfg.GRID_BIAS_Y
    bottom_border_h = cfg.GRID_BIAS_Y + cfg.GRID_HEIGHT
    num_blocks_height = (bottom_border_h - top_border_h) // cfg.BLOCK_HEIGHT

    pt1, pt2 = (left_border_w, top_border_h), (right_border_w, bottom_border_h)

    grid = np.zeros((num_blocks_width, num_blocks_height))
    coords = []
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            coords.append([y, x])
    
    random.shuffle(coords)

    coords = coords[:cfg.BLOCKS_NUM]
    for y, x in coords:
        grid[x, y] = 1

    return grid, (pt1, pt2)

def draw_block(img, coords: tuple[int, int]):
    '''
    coords = (0, 2)
    base_points = (left_border_w, top_border_h), (right_border_w, bottom_border_h)
    '''
    pt1 = (cfg.GRID_BIAS_X + cfg.BLOCK_WIDTH * coords[0],
           cfg.GRID_BIAS_Y + cfg.BLOCK_HEIGHT * (coords[1]))

    pt2 = (cfg.GRID_BIAS_X + cfg.BLOCK_WIDTH * (coords[0] + 1),
           cfg.GRID_BIAS_Y + cfg.BLOCK_HEIGHT * (coords[1] + 1))

    cv2.rectangle(img, pt1, pt2, [255,0,0], -1)
    cv2.rectangle(img, pt1, pt2, [0,0,0], 4)


def draw_grid(img, grid):

    grid_shape = grid.shape
    for y in range(grid_shape[0]):
        for x in range(grid_shape[1]):
            if grid[y, x]:
                draw_block(img, (x,y))

    # quit()
    # draw_block(img, (0, 2), points)
    

# if __name__ == '__main__':
#     draw_grid()