"""
Calculate forces in joints

"""

import numpy as np

ANGLE = np.pi / 3
FORCE_DOWN = 36.6
FORCE_UP_REACTION = 128
ITERATIONS = 10


def loop(length, force_up, force_down):
    temp = init_forces(force_up)

    yl = temp[1]
    xl = temp[0]
    yu = force_y_upper(yl)
    xu = force_x_upper(0, yl, yu)

    print('Y lower 0 :', yl, '\nX lower 0 :', xl, '\nY upper 0 :', yu, '\nX upper 0 :', xu)

    x_upper = [xu]
    x_lower = [xl]
    y_lower = [yl]
    y_upper = [yu]

    for i in range(length):
        yl_t = force_y_lower(y_upper[-1], force_down)
        y_lower.append(yl_t)
        print('Y lower', (i+1), ':', yl_t)

        xl_t = force_x_lower(x_lower[-1], y_upper[-1], y_lower[-1])
        x_lower.append(xl_t)
        print('X lower', (i + 1), ':', xl_t)

        yu_t = force_y_upper(y_lower[-1])
        y_upper.append(yu_t)
        print('Y upper', (i + 1), ':', yu_t)

        xu_t = force_x_upper(x_upper[-1], y_lower[-1], y_upper[-1])
        x_upper.append(xu_t)
        print('X upper', (i + 1), ':', xu_t)

    return x_upper, x_lower, y_lower, y_upper


def init_forces(force_up):
    as_ = np.sin(ANGLE)
    ac_ = np.cos(ANGLE)

    y = (1/as_) * force_up

    x = ac_ * y

    return x, (-1*y)


def force_x_lower(known_horizontal, known_vertical_1, known_vertical_2):
    a = np.cos(ANGLE)

    unknown = a * abs(known_vertical_1) + a * abs(known_vertical_2) + abs(known_horizontal)
    return unknown


def force_x_upper(known_horizontal, known_vertical_1, known_vertical_2):
    a = np.cos(ANGLE)

    unknown = a * abs(known_vertical_1) + a * abs(known_vertical_2) + abs(known_horizontal)
    return -1 * unknown


def force_y_lower(known, force_down):
    a = np.sin(ANGLE)

    unknown = (1/a) * (abs(known) * a - force_down)
    return -1 * unknown


def force_y_upper(known):
    a = np.sin(ANGLE)
    unknown = (1 / a) * (abs(known) * a)
    return unknown


if __name__ == '__main__':
    a = loop(ITERATIONS - 1, FORCE_UP_REACTION, FORCE_DOWN)

    for i in range(len(a)):
        print(a[i])


