def cmy_rgb(r, g, b):
    return 1 - r, 1 - g, 1 - b


def cmy_cmyk(c, m, y):
    b = min(c, m, y)
    return c - b, m - b, y - b, b


def cmyk_cmy(c, m, y, k):
    return c + k, m + k, y + k,
