import random
import numpy as np
import pygame
from Constants import CONSTANTS
from DominoManager import DominoManager


class Diamond:
    """
    Diamond initializer and drawer
    """
    diamond = None
    tiling = None
    screen = None
    font = None
    clock = None
    grid_rects = None
    tiles = []

    def __init__(self, order, speed=1, const: CONSTANTS = CONSTANTS()):
        self.const = const
        self.order = order
        self.speed = speed

        self.init_diamond_array()
        self.init_pygame()
        self.init_grid_rects()

    def init_diamond_array(self):
        ndarray = np.triu(np.ones([self.order] * 2))
        self.diamond = np.concatenate([
            np.concatenate(
                [np.flipud(ndarray), np.transpose(ndarray)], axis=1),
            np.concatenate([ndarray, np.fliplr(ndarray)], axis=1)
        ], axis=0)
        self.tiling = np.zeros(2 * [2 * self.order], dtype='O')

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.const.DISPLAY_MODE)
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 32)
        self.clock = pygame.time.Clock()

    def init_grid_rects(self):
        self.grid_rects = []
        for i in range(self.order):
            left = self.const.SCREEN_SIZE / 2 * (i + 1) / (self.order + 1)
            top = self.const.SCREEN_SIZE / 2 * (1 - (i + 1) / (self.order + 1))
            width = self.const.SCREEN_SIZE \
                    * (self.order - i) / (self.order + 1)
            height = self.const.SCREEN_SIZE * (i + 1) / (self.order + 1)
            self.grid_rects.append(
                pygame.Rect(
                    left, top, width, height
                )
            )

    def step_tile_generation(self, draw: bool = False):
        self.update_order()
        if draw:
            self.draw()
        self.remove_opposing()
        if draw:
            self.draw()
        self.move_tiles()
        if draw:
            self.draw()
        self.fill_empty_squares()
        if draw:
            self.draw()

    def update_order(self):
        self.order += 1

        tiling = self.tiling
        self.init_diamond_array()
        self.tiling[1:-1, 1:-1] = tiling

        self.init_grid_rects()
        for tile in self.tiles:
            tile.gen_rect(order=self.order)

    def remove_opposing(self):
        for x, y in zip(*np.where(self.diamond)):
            tile = self.tiling[x, y]
            if tile == 0:
                continue
            i2, j2 = np.array([x, y]) + self.const.TILE_STEPS[tile.orientation]
            if not (0 <= i2 <= 2 * self.order and 0 <= j2 <= 2 * self.order):
                continue
            neighbour_tile = self.tiling[i2, j2]
            if neighbour_tile == 0:
                continue
            if neighbour_tile.orientation == self.const.TILE_STEP_CONFLICTS[
                tile.orientation
            ]:
                self.tiling[np.where(self.tiling == tile)] = 0
                self.tiling[np.where(self.tiling == neighbour_tile)] = 0
                self.tiles.remove(tile)
                self.tiles.remove(neighbour_tile)

    def move_tiles(self):
        self.tiling = np.zeros([2 * self.order] * 2, dtype='O')
        for tile in self.tiles:
            tile.step()
            tile.gen_rect(order=self.order)
            self.tiling[tuple(tile.upper_left_corner + self.order)] = tile
            self.tiling[
                tuple(tile.upper_left_corner + self.order + (
                    self.const.TILE_STEPS[1] if tile.orientation in (2, 3)
                    else self.const.TILE_STEPS[2]))
            ] = tile

    def fill_empty_squares(self):
        while np.any((self.tiling == 0) & (self.diamond == 1)):
            ii, jj = [i[0] for i in np.where(
                (self.tiling == 0) & (self.diamond == 1)
            )]
            if random.random() < 0.5:
                first_tile, second_tile = self.fill(ii, jj)
            else:
                first_tile, second_tile = self.fill(ii, jj,
                                                    is_horizontal=False)
            self.tiles.append(first_tile)
            self.tiles.append(second_tile)

    def fill(self,
             xx, yy,
             is_horizontal: bool = True,
             first_orientation: int = 3, second_orientation: int = 2,
             first_adding: int = 1, second_adding: int = 0):
        """
        Additional method for code reducing
        :param xx: xx coordinate
        :param yy: yy coordinate
        :param is_horizontal: is tile orientation horizontal
        :param first_orientation: 0, 1, 2 or 3
        :param second_orientation: 0, 1, 2 or 3
        :param first_adding: adding depending on the orientation
        :param second_adding: adding depending on the orientation
        :return: first (without shift) and second (with shift) tiles
        """
        if not is_horizontal:
            first_orientation, second_orientation = 0, 1
            first_adding, second_adding = 0, 1

        first_tile = DominoManager(
            (xx - self.order, yy - self.order),
            first_orientation,
            self.order
        )

        self.tiling[xx, yy] = first_tile
        self.tiling[xx + first_adding, yy + second_adding] = first_tile

        second_tile = DominoManager(
            (xx - self.order + second_adding, yy - self.order + first_adding),
            second_orientation,
            self.order
        )

        self.tiling[xx + second_adding, yy + first_adding] = second_tile
        self.tiling[xx + 1, yy + 1] = second_tile
        return first_tile, second_tile

    def draw(self):
        """

        :return:
        """
        self.handle_events()
        self.screen.fill(self.const.BACKGROUND_COLOR)
        self.draw_grid()
        self.draw_tiles()
        self.draw_annotations()
        pygame.display.flip()

    def handle_events(self):
        if self.speed is not None:
            self.clock.tick(self.speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def draw_grid(self):
        for rect in self.grid_rects:
            pygame.draw.rect(self.screen, rect=rect,
                             color=self.const.TILE_COLORS[None])
        pygame.draw.line(
            self.screen,
            color=self.const.BORDER_COLOR,
            start_pos=(
                self.const.SCREEN_SIZE / 2 * (self.order + 1),
                self.const.SCREEN_SIZE / 2
            ),
            end_pos=(
                self.const.SCREEN_SIZE / 2 * (
                        1 + self.order / (self.order + 1)),
                self.const.SCREEN_SIZE / 2
            ),
            width=self.const.BORDER_WIDTH
        )
        pygame.draw.line(
            self.screen,
            color=self.const.BORDER_COLOR,
            start_pos=(
                self.const.SCREEN_SIZE / 2,
                self.const.SCREEN_SIZE / 2 * (self.order + 1)
            ),
            end_pos=(
                self.const.SCREEN_SIZE / 2,
                self.const.SCREEN_SIZE / 2 * (
                        1 + self.order / (self.order + 1))
            ),
            width=self.const.BORDER_WIDTH
        )
        for rect in self.grid_rects:
            pygame.draw.rect(
                self.screen,
                rect=rect,
                color=self.const.BORDER_COLOR,
                width=self.const.BORDER_WIDTH
            )

    def draw_tiles(self):
        for tile in self.tiles:
            pygame.draw.rect(
                self.screen,
                rect=tile.rect,
                color=self.const.TILE_COLORS[tile.orientation]
            )
            pygame.draw.rect(
                self.screen,
                rect=tile.rect,
                color=self.const.BORDER_COLOR, width=self.const.BORDER_WIDTH
            )

    def draw_annotations(self):
        source = self.font.render(
            f'{self.order}',
            True,
            self.const.TILE_COLORS[None]
        )
        self.screen.blit(
            source,
            np.array([self.const.SCREEN_SIZE, 0]).astype(int)
            + [-source.get_width(), 0])
