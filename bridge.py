from math import *

"""

Variables
"""

joints_per_side = 0
total_weight = 0
force_member = 0
length_member = 0

HSS_I = 550
HSS_A = 344
HSS_r = 150

"""
0. force (kN), 1. length (mm)
"""
members = [
    [28.5, 3500],
    [19.5, 2000]
]

HSS = [HSS_I, HSS_A, HSS_r]


def test_hss(members, hss, stress_max, E):
    hss_i = hss[0]
    hss_a = hss[1]
    hss_r = hss[2]

    for i in range(len(members)):
        member = members[i]
        force = member[0]
        length = member[1]

        if test_integrity(calculate_a(force, stress_max), hss_a) and test_integrity(calculate_i(force, length, E),
                                                                                    hss_i) and test_integrity(
                calculate_r(length), hss_r):
            val = "Pass"
        elif not test_integrity(calculate_a(force, stress_max), hss_a):
            val = "Failure A"
        elif not test_integrity(calculate_i(force, length, E), hss_i):
            val = "Failure I"
        elif not test_integrity(calculate_r(length), hss_r):
            val = "Failure r"

        print("Member " + str(i) + ": " + val)


def calculate_i(force, length, E, fos=3):
    I = (fos * force * length ** 2) / (E * pi ** 2)
    return I


def calculate_a(force, stress, fos=2):
    A = fos * force / stress
    return A


def calculate_r(L):
    return L / 200


def test_integrity(max_allowed_value, actual_value):
    return max_allowed_value <= actual_value


test_hss(members, HSS, 350, 200000)
