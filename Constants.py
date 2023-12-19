import numpy as np
from pygame.color import THECOLORS


class CONSTANTS:
    DISPLAY_MODE = [800, 800]
    SCREEN_SIZE = 800
    BACKGROUND_COLOR = THECOLORS['darkgrey']
    BORDER_COLOR = THECOLORS['darkgrey']
    BORDER_WIDTH = 1
    ORIENTATIONS = range(4)
    TILE_COLORS = {
        0: THECOLORS['blue'],
        1: THECOLORS['green'],
        2: THECOLORS['red'],
        3: THECOLORS['yellow'],
        None: (200,) * 3
    }
    TILE_STEPS = {
        0: np.array([-1, 0]),
        1: np.array([1, 0]),
        2: np.array([0, 1]),
        3: np.array([0, -1]),
    }
    TILE_STEP_CONFLICTS = {
        0: 1,
        1: 0,
        2: 3,
        3: 2,
    }

    def set_tile_colors(self, mode: str = '_default'):
        if mode == '_default':
            self.TILE_COLORS = {
                0: THECOLORS['blue'],
                1: THECOLORS['green'],
                2: THECOLORS['red'],
                3: THECOLORS['yellow'],
                None: (200,) * 3
            }
        elif mode == '_dark_default':
            self.TILE_COLORS = {
                0: THECOLORS['darkblue'],
                1: THECOLORS['darkgreen'],
                2: THECOLORS['darkred'],
                3: THECOLORS['yellow4'],
                None: (200,) * 3
            }
        elif mode == '_pink_blue_soft':
            self.TILE_COLORS = {
                0: THECOLORS['lightblue'],
                1: THECOLORS['purple'],
                2: THECOLORS['pink'],
                3: THECOLORS['blue'],
                None: (200,) * 3
            }
        elif mode == '_green':
            self.TILE_COLORS = {
                0: THECOLORS['palegreen'],
                1: THECOLORS['darkgreen'],
                2: THECOLORS['seagreen'],
                3: THECOLORS['yellowgreen'],
                None: (200,) * 3
            }
        elif mode == '_red_orange':
            self.TILE_COLORS = {
                0: THECOLORS['orangered'],
                1: THECOLORS['orangered4'],
                2: THECOLORS['darkred'],
                3: THECOLORS['orangered3'],
                None: (200,) * 3
            }
        elif mode == '_grey':
            self.TILE_COLORS = {
                0: THECOLORS['lightgrey'],
                1: THECOLORS['gray50'],
                2: THECOLORS['grey1'],
                3: THECOLORS['grey25'],
                None: (200,) * 3
            }
        elif mode == '_blue':
            self.TILE_COLORS = {
                0: THECOLORS['lightblue'],
                1: THECOLORS['slateblue'],
                2: THECOLORS['cornflowerblue'],
                3: THECOLORS['deepskyblue'],
                None: (200,) * 3
            }
        elif mode == '_dark_blue':
            self.TILE_COLORS = {
                0: THECOLORS['mediumslateblue'],
                1: THECOLORS['midnightblue'],
                2: THECOLORS['darkblue'],
                3: THECOLORS['darkslateblue'],
                None: (200,) * 3
            }
        elif mode == '_pink':
            self.TILE_COLORS = {
                0: THECOLORS['hotpink2'],
                1: THECOLORS['deeppink'],
                2: THECOLORS['pink1'],
                3: THECOLORS['pink2'],
                None: (200,) * 3
            }
        elif mode == '_purple_yellow':
            self.TILE_COLORS = {
                0: THECOLORS['purple'],
                1: THECOLORS['mediumorchid'],
                2: THECOLORS['yellow'],
                3: THECOLORS['yellow2'],
                None: (200,) * 3
            }


    """dict_keys(['aliceblue', 'antiquewhite', 'antiquewhite1', 
    'antiquewhite2', 'antiquewhite3', 'antiquewhite4', 'aqua', 'aquamarine', 
    'aquamarine1', 'aquamarine2', 'aquamarine3', 'aquamarine4', 'azure', 
    'azure1', 'azure3', 'azure2', 'azure4', 'beige', 'bisque', 'bisque1', 
    'bisque2', 'bisque3', 'bisque4', 'black', 'blanchedalmond', 'blue', 
    'blue1', 'blue2', 'blue3', 'blue4', 'blueviolet', 'brown', 'brown1', 
    'brown2', 'brown3', 'brown4', 'burlywood', 'burlywood1', 'burlywood2', 
    'burlywood3', 'burlywood4', 'cadetblue', 'cadetblue1', 'cadetblue2', 
    'cadetblue3', 'cadetblue4', 'chartreuse', 'chartreuse1', 'chartreuse2', 
    'chartreuse3', 'chartreuse4', 'chocolate', 'chocolate1', 'chocolate2', 
    'chocolate3', 'chocolate4', 'coral', 'coral1', 'coral2', 'coral3', 
    'coral4', 'cornflowerblue', 'cornsilk', 'cornsilk1', 'cornsilk2', 
    'cornsilk3', 'cornsilk4', 'crimson', 'cyan', 'cyan1', 'cyan2', 'cyan3', 
    'cyan4', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgoldenrod1', 
    'darkgoldenrod2', 'darkgoldenrod3', 'darkgoldenrod4', 'darkgray', 
    'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 
    'darkolivegreen1', 'darkolivegreen2', 'darkolivegreen3', 
    'darkolivegreen4', 'darkorange', 'darkorange1', 'darkorange2', 
    'darkorange3', 'darkorange4', 'darkorchid', 'darkorchid1', 
    'darkorchid2', 'darkorchid3', 'darkorchid4', 'darkred', 'darksalmon', 
    'darkseagreen', 'darkseagreen1', 'darkseagreen2', 'darkseagreen3', 
    'darkseagreen4', 'darkslateblue', 'darkslategray', 'darkslategray1', 
    'darkslategray2', 'darkslategray3', 'darkslategray4', 'darkslategrey', 
    'darkturquoise', 'darkviolet', 'deeppink', 'deeppink1', 'deeppink2', 
    'deeppink3', 'deeppink4', 'deepskyblue', 'deepskyblue1', 'deepskyblue2', 
    'deepskyblue3', 'deepskyblue4', 'dimgray', 'dimgrey', 'dodgerblue', 
    'dodgerblue1', 'dodgerblue2', 'dodgerblue3', 'dodgerblue4', 'firebrick', 
    'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floralwhite', 
    'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'gold1', 
    'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 
    'goldenrod3', 'goldenrod4', 'gray', 'gray0', 'gray1', 'gray100', 'green',
    'green4', 'greenyellow', 'grey', 'grey0',  
    'grey100', 'honeydew', 'honeydew1', 'honeydew2', 'honeydew3', 
    'honeydew4', 'hotpink', 'hotpink1', 'hotpink2', 'hotpink3', 'hotpink4', 
    'indianred', 'indianred1', 'indianred2', 'indianred3', 'indianred4', 
    'indigo', 'ivory', 'ivory1', 'ivory2', 'ivory3', 'ivory4', 'khaki', 
    'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavenderblush', 
    'lavenderblush1', 'lavenderblush2', 'lavenderblush3', 'lavenderblush4', 
    'lawngreen', 'lemonchiffon', 'lemonchiffon1', 'lemonchiffon2', 
    'lemonchiffon3', 'lemonchiffon4', 'lightblue', 'lightblue1', 
    'lightblue2', 'lightblue3', 'lightblue4', 'lightcoral', 'lightcyan', 
    'lightcyan1', 'lightcyan2', 'lightcyan3', 'lightcyan4', 
    'lightgoldenrod', 'lightgoldenrod1', 'lightgoldenrod2', 
    'lightgoldenrod3', 'lightgoldenrod4', 'lightgoldenrodyellow', 
    'lightgray', 'lightgreen', 'lightgrey', 'lightpink', 'lightpink1', 
    'lightpink2', 'lightpink3', 'lightpink4', 'lightsalmon', 'lightsalmon1', 
    'lightsalmon2', 'lightsalmon3', 'lightsalmon4', 'lightseagreen', 
    'lightskyblue', 'lightskyblue1', 'lightskyblue2', 'lightskyblue3', 
    'lightskyblue4', 'lightslateblue', 'lightslategray', 'lightslategrey', 
    'lightsteelblue', 'lightsteelblue1', 'lightsteelblue2', 
    'lightsteelblue3', 'lightsteelblue4', 'lightyellow', 'lightyellow1', 
    'lightyellow2', 'lightyellow3', 'lightyellow4', 'linen', 'lime', 
    'limegreen', 'magenta', 'magenta1', 'magenta2', 'magenta3', 'magenta4', 
    'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 
    'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumorchid1', 
    'mediumorchid2', 'mediumorchid3', 'mediumorchid4', 'mediumpurple', 
    'mediumpurple1', 'mediumpurple2', 'mediumpurple3', 'mediumpurple4', 
    'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 
    'mediumturquoise', 'mediumvioletred', 'midnightblue', 'mintcream', 
    'mistyrose', 'mistyrose1', 'mistyrose2', 'mistyrose3', 'mistyrose4', 
    'moccasin', 'navajowhite', 'navajowhite1', 'navajowhite2', 
    'navajowhite3', 'navajowhite4', 'navy', 'navyblue', 'oldlace', 'olive', 
    'olivedrab', 'olivedrab1', 'olivedrab2', 'olivedrab3', 'olivedrab4', 
    'orange', 'orange1', 'orange2', 'orange3', 'orange4', 'orangered', 
    'orangered1', 'orangered2', 'orangered3', 'orangered4', 'orchid', 
    'orchid1', 'orchid2', 'orchid3', 'orchid4', 'palegreen', 'palegreen1', 
    'palegreen2', 'palegreen3', 'palegreen4', 'palegoldenrod', 
    'paleturquoise', 'paleturquoise1', 'paleturquoise2', 'paleturquoise3', 
    'paleturquoise4', 'palevioletred', 'palevioletred1', 'palevioletred2', 
    'palevioletred3', 'palevioletred4', 'papayawhip', 'peachpuff', 
    'peachpuff1', 'peachpuff2', 'peachpuff3', 'peachpuff4', 'peru', 'pink', 
    'pink1', 'pink2', 'pink3', 'pink4', 'plum', 'plum1', 'plum2', 'plum3', 
    'plum4', 'powderblue', 'purple', 'purple1', 'purple2', 'purple3', 
    'purple4', 'red', 'red1', 'red2', 'red3', 'red4', 'rosybrown', 
    'rosybrown1', 'rosybrown2', 'rosybrown3', 'rosybrown4', 'royalblue', 
    'royalblue1', 'royalblue2', 'royalblue3', 'royalblue4', 'salmon', 
    'salmon1', 'salmon2', 'salmon3', 'salmon4', 'saddlebrown', 'sandybrown', 
    'seagreen', 'seagreen1', 'seagreen2', 'seagreen3', 'seagreen4', 
    'seashell', 'seashell1', 'seashell2', 'seashell3', 'seashell4', 
    'sienna', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'silver', 
    'skyblue', 'skyblue1', 'skyblue2', 'skyblue3', 'skyblue4', 'slateblue', 
    'slateblue1', 'slateblue2', 'slateblue3', 'slateblue4', 'slategray', 
    'slategray1', 'slategray2', 'slategray3', 'slategray4', 'slategrey', 
    'snow', 'snow1', 'snow2', 'snow3', 'snow4', 'springgreen', 
    'springgreen1', 'springgreen2', 'springgreen3', 'springgreen4', 
    'steelblue', 'steelblue1', 'steelblue2', 'steelblue3', 'steelblue4', 
    'tan', 'tan1', 'tan2', 'tan3', 'tan4', 'teal', 'thistle', 'thistle1', 
    'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato1', 'tomato2', 
    'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 
    'turquoise3', 'turquoise4', 'violet', 'violetred', 'violetred1', 
    'violetred2', 'violetred3', 'violetred4', 'wheat', 'wheat1', 'wheat2', 
    'wheat3', 'wheat4', 'white', 'whitesmoke', 'yellow', 'yellow1', 
    'yellow2', 'yellow3', 'yellow4', 'yellowgreen']) 
    """
