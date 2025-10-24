
import config as cfg
import cv2


def draw_ball(img):
    center_point_x = cfg.WINDOW_WIDTH // 2
    if (center_point_x != cfg.WINDOW_WIDTH or center_point_x != 0):
        center_point_x += cfg.BALL_SPEED
    

    center_point_y = cfg.WINDOW_HEIGHT - cfg.PLAYER_POS - cfg.PLAYER_HEIGHT - cfg.BALL_R



    pt = (center_point_x, center_point_y)
    cv2.circle(img = img, center = pt, radius = cfg.BALL_R, color = (128,0,128), thickness = -1)