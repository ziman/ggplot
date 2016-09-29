class position(object):
    """
        Identity position. Does not change anything.
    """

    def _transform(self, xy):
        return xy

def as_position(x):
    if isinstance(x, position):
        return x
    elif x is None:
        return position()
    else:
        raise ValueError('cannot coerce to position: %s' % x)
