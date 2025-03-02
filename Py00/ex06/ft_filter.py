class ft_filter(object):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    def __init__(self, function, lst):
        if function is None:
            self.tab = [x for x in lst if x is True]
        else:
            self.tab = [x for x in lst if function(x) is True]

    def __iter__(self):
        return self.tab.__iter__()
    tab = []
