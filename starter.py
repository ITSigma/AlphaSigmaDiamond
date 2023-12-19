from AztecDiamond import Diamond
from Constants import CONSTANTS
import argparse


class Starter:
    def __init__(self):
        self.constants = CONSTANTS()
        self.parsed_args = self.parser()
        self.diamond = None
        self.grow_mode = self.parsed_args.grow
        self.set_palette_mode()
        if self.grow_mode:
            self.grow_diamond()
        else:
            self.draw_diamond_by_order()

    def set_palette_mode(self):
        self.constants.set_tile_colors(self.parsed_args.palette)

    def init_diamond(self):
        self.diamond = Diamond(order=1,
                               speed=self.parsed_args.speed,
                               const=self.constants)
        self.diamond.draw()
        self.diamond.fill_empty_squares()
        self.diamond.draw()

    def draw_diamond_by_order(self):
        self.diamond = Diamond(order=1,
                               speed=1000,
                               const=self.constants)
        self.diamond.fill_empty_squares()
        if self.parsed_args.order > 2:
            for _ in range(self.parsed_args.order - 2):
                self.diamond.step_tile_generation(draw=False)
        self.diamond.step_tile_generation(draw=True)

    def grow_diamond(self):
        self.init_diamond()
        for _ in range(self.parsed_args.order - 1):
            self.diamond.step_tile_generation(draw=True)

    @staticmethod
    def parser():
        args = argparse.ArgumentParser()

        args.add_argument(
            '-o',
            '--order',
            type=int,
            default=50
        )

        args.add_argument(
            '-s',
            '--speed',
            type=int,
            default=100
        )

        args.add_argument(
            '-m',
            '--palette',
            choices=['_default', '_pink_blue_soft', '_green', '_grey',
                     '_red_orange', '_blue', '_dark_blue', '_dark_default',
                     '_pink', '_purple_yellow'],
            type=str,
            default='_default'
        )

        args.add_argument(
            '-g',
            '--grow',
            action='store_true',
            default=False
        )
        return args.parse_args()


def main():
    starter = Starter()

    while True:
        starter.diamond.handle_events()


if __name__ == '__main__':
    main()
