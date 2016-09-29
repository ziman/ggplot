from .position import position

import numpy as np

class position_jitter(position):
    """
        Add jitter to spread out overcrowded areas. Useful with alpha < 1.0.

        Parameters:
            <name>: (type) [default]
            ------------------------
            kind:   ('addictive' | 'multiplicative')  ['additive']
            size:   (float) [0.5]
            range:  (float, float) [0, size]
            range_x: (float, float) [range]
            range_y: (float, float) [range]
    """

    def __init__(self,
            kind='additive', size=0.5, range=None,
            range_x=None, range_y=None):
        self.kind = kind
        self.size = size
        self.range = range or (0, kind)
        self.range_x = range_x or range
        self.range_y = range_y or range

    def _transform(self, xy):
        rx_lo, rx_hi = self.range_x
        ry_lo, ry_hi = self.range_y

        if self.kind == 'additive':
            return (
                xy[0] + np.random.uniform(rx_lo, rx_hi, len(xy[0])),
                xy[1] + np.random.uniform(ry_lo, ry_hi, len(xy[1])),
            )
        elif self.kind == 'multiplicative':
            return (
                xy[0] * np.random.uniform(rx_lo, rx_hi, len(xy[0])),
                xy[1] * np.random.uniform(ry_lo, ry_hi, len(xy[1])),
            )
        else:
            raise ValueError("unknown jitter kind: %s" % self.kind)
