"""
Calculate forces in joints

"""

import numpy as np

ANGLE = np.pi / 6
FORCE_DOWN = 36.6
FORCE_UP_REACTION = 128
ITERATIONS = 10


def loop(length, force_up, force_down):
    temp = init_forces(force_up)

    yd = temp[1]
    xl = temp[0]
    yv = force_y_vertical(yd)
    xu = force_x_upper(0, yd)

    print('Y lower 0 :', yd, '\nX lower 0 :', xl, '\nY upper 0 :', yv, '\nX upper 0 :', xu)

    x_upper = [xu]
    x_lower = [xl]
    y_lower = [yd]
    y_upper = [yv]

    for i in range(length):
        yl_t = force_y_diagonal(y_upper[-1], force_down)
        y_lower.append(yl_t)
        print('Y lower', (i+1), ':', yl_t)

        xl_t = force_x_lower(x_lower[-1], y_upper[-1], y_lower[-1])
        x_lower.append(xl_t)
        print('X lower', (i + 1), ':', xl_t)

        yu_t = force_y_vertical(y_lower[-1])
        y_upper.append(yu_t)
        print('Y upper', (i + 1), ':', yu_t)

        xu_t = force_x_upper(x_upper[-1], y_lower[-1], y_upper[-1])
        x_upper.append(xu_t)
        print('X upper', (i + 1), ':', xu_t)


def init_forces(force_up):
    as_ = np.sin(ANGLE)
    ac_ = np.cos(ANGLE)

    y = (1/as_) * force_up

    x = ac_ * y

    return x, (-1*y)


def force_x_lower(known_horizontal, diagonal):
    a = np.cos(ANGLE)

    unknown = abs(known_horizontal) - a * abs(diagonal)
    return unknown


def force_x_upper(known_horizontal, diagonal):
    a = np.cos(ANGLE)

    unknown = a * abs(diagonal) + abs(known_horizontal)
    return -1 * unknown


def force_y_diagonal(known, force_down):
    a = np.sin(ANGLE)

    unknown = (1/a) * (abs(known) - force_down)
    return -1 * unknown


def force_y_vertical(known):
    a = np.sin(ANGLE)
    unknown = abs(known) * a
    return unknown


if __name__ == '__main__':
    loop(ITERATIONS - 1, FORCE_UP_REACTION, FORCE_DOWN)
