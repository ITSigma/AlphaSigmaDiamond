from Constants import CONSTANTS
import numpy as np
import pygame


class DominoManager:
    def __init__(self, upper_left_corner, orientation, order=None):
        assert orientation in CONSTANTS.ORIENTATIONS
        self.upper_left_corner = np.array(upper_left_corner)
        self.orientation = orientation
        self.rect = None

        if order is not None:
            self.gen_rect(order=order)

    def gen_rect(self, order):
        grid_size = CONSTANTS.SCREEN_SIZE / 2 / (order + 1)
        top = round(grid_size * (order + 1 + self.upper_left_corner[1]))
        left = round(grid_size * (order + 1 + self.upper_left_corner[0]))
        height = round(grid_size * (2 if self.orientation in (0, 1) else 1))
        width = round(grid_size * (1 if self.orientation in (0, 1) else 2))
        self.rect = pygame.Rect(top, left, height, width)

    def step(self):
        self.upper_left_corner += CONSTANTS.TILE_STEPS[self.orientation]
