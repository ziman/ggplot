from .geom_point import geom_point


class geom_jitter(geom_point):
    """
    Same as geom_point but with randomness added so you can see the points better.

    This jitter is additive, uniformly distributed within the given radius.

    Parameters
    ----------
    x:
        x values for (x, y) coordinates
    y:
        y values for (x, y) coordinates
    color:
        color of points
    alpha:
        transparency of color
    shape:
        type of point used ('o', '^', 'D', 'v', 's', '*', 'p', '8', "_", "|", "_")
    edgecolors:
        color of the outer line of the point
    size:
        size of the point
    radius:
        jitter radius [0.5]
    radius_x:
        jitter radius along the x axis [radius]
    radius_y:
        jitter radius along the y axis [radius]

    Examples
    --------
    """
    def __init__(self, radius=0.5, radius_x=None, radius_y=None, **kwargs):
        super(geom_point, self).__init__(*args, **kwargs)
        self.params['position'] = "jitter"
        self.params['jitter_radius'] = (radius_x or radius, radius_y or radius)
