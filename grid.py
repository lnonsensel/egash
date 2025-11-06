import numpy as np
import config as cfg
import cv2

import random
from dataclasses import dataclass, field

@dataclass
class Block:
    p1: tuple[int, int]
    p2: tuple[int, int]
    is_hidden: bool

@dataclass
class GridState:
    grid: np.ndarray
    num_blocks_width: int 
    num_blocks_height: int
    coords: list = field(default_factory = list)
    block_coords: list = field(default_factory = list)

    def grid_is_empty(self):
        print(self.grid, not np.any(self.grid))
        return not np.any(self.grid) 


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
            coords.append([x,y])
    
    
    random.shuffle(coords)

    coords = coords[:cfg.BLOCKS_NUM]
    for y, x in coords:
        grid[y, x] = 1

    block_windows_poss = [get_block_window_pos(coord) for coord in coords]
    state = GridState(grid=grid,
                      num_blocks_width = num_blocks_width,
                      num_blocks_height = num_blocks_height,
                      coords = coords,
                      block_coords = block_windows_poss)
    return state

def get_block_window_pos(coords: tuple[int, int]):
    
    pt1 = (cfg.GRID_BIAS_X + cfg.BLOCK_WIDTH * coords[0],
           cfg.GRID_BIAS_Y + cfg.BLOCK_HEIGHT * (coords[1]))

    pt2 = (cfg.GRID_BIAS_X + cfg.BLOCK_WIDTH * (coords[0] + 1),
           cfg.GRID_BIAS_Y + cfg.BLOCK_HEIGHT * (coords[1] + 1))

    return pt1, pt2

def draw_block(img, coords: tuple[int, int]):
    '''
    coords = (0, 2)
    base_points = (left_border_w, top_border_h), (right_border_w, bottom_border_h)
    '''
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pt1, pt2 = get_block_window_pos(coords)
    #cv2.rectangle(img, pt1, pt2, [255,0,0], -1)
    cv2.rectangle(img, pt1, pt2, [b,g,r], -1)
    cv2.rectangle(img, pt1, pt2, [255,255,255], 1)


def draw_grid(img, state: GridState):
    grid = state.grid
    grid_shape = grid.shape
    for x in range(grid_shape[0]):
        for y in range(grid_shape[1]):
            if grid[x,y]:
                draw_block(img, (x,y))

    # quit()
    # draw_block(img, (0, 2), points)
    

# if __name__ == '__main__':
#     draw_grid()
def draw_grid_box(img):
    right_border_w = cfg.WINDOW_WIDTH - cfg.GRID_BIAS_X
    left_border_w = cfg.GRID_BIAS_X
    

    top_border_h = cfg.GRID_BIAS_Y
    bottom_border_h = cfg.GRID_BIAS_Y + cfg.GRID_HEIGHT
    
    cv2.rectangle(img=img ,pt1 =  (left_border_w,top_border_h), pt2=(right_border_w,bottom_border_h), color = (100,100,100), thickness= 1) 
