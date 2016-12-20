RAW_PROB = {
    3: 0.46,
    4: 1.39,
    5: 2.78,
    6: 4.63,
    7: 6.94,
    8: 9.72,
    9: 11.57,
    10: 12.5,
    11: 12.5,
    12: 11.57,
    13: 9.72,
    14: 6.94,
    15: 4.63,
    16: 2.78,
    17: 1.39,
    18: 0.46,
}

PROB = {
    3: 100.00,
    4: 99.54,
    5: 98.15,
    6: 95.37,
    7: 90.74,
    8: 83.80,
    9: 74.07,
    10: 62.50,
    11: 50.00,
    12: 37.50,
    13: 25.93,
    14: 16.20,
    15: 9.26,
    16: 4.63,
    17: 1.85,
    18: 0.46,
}

def chance_of_success(tn, mod=0, crit_fail=False, crit_succeed=False):
    abs_tn = tn - mod

    if abs_tn <= 3:
        if crit_fail:
            return 99.54

        else:
            return 100.0

    if abs_tn > 18:
        if crit_succeed:
            return 0.46

        else:
            return 0.0

    return PROB[abs_tn]
