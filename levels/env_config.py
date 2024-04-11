import numpy as np

# 0: normal tile
# 1: orange tile
# 2: circle switch
# 3: x switch
# 4: goal
# 5:
# 8: block
# 9: none

# Level 1:
level_one_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 4, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

# Level 2:
level_two_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 3, 0, 9, 9, 0, 4, 0, 9, 9, 9],
        [9, 9, 0, 0, 2, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

level_two_soft_switches = np.array(
    [{"switch_location": (4, 4), "toggle_tiles": [(6, 6), (6, 7)], "mode": "toggle"}]
)


level_two_hard_switches = np.array(
    [{"switch_location": (3, 10), "toggle_tiles": [(6, 12), (6, 13)]}]
)

# Level 3:
level_three_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 4, 0, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

# Level 4:
level_four_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 1, 1, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 0, 0, 0, 0, 1, 1, 1, 1, 1, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 0, 0, 0, 0, 1, 1, 1, 1, 1, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 4, 0, 9, 9, 1, 1, 0, 1, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 1, 1, 1, 1, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

# Level 5:
level_five_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9],
        [9, 9, 9, 0, 0, 2, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 2, 9, 9, 9],
        [9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9],
        [9, 9, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

level_five_soft_switches = np.array(
    [
        {
            "switch_location": (2, 10),
            "toggle_tiles": [(2, 7), (2, 8)],
            "mode": "toggle",
        },
        {
            "switch_location": (7, 16),
            "toggle_tiles": [(9, 7), (9, 8)],
            "mode": "toggle",
        },
        {"switch_location": (6, 8), "toggle_tiles": [(9, 7), (9, 8)], "mode": "off"},
        {"switch_location": (4, 5), "toggle_tiles": [(9, 7), (9, 8)], "mode": "on"},
    ]
)

# Level 6:
level_six_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 4, 0, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

# Level 7:
level_seven_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9, 0, 9, 9, 0, 0, 0, 0, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 4, 0, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 3, 9, 9, 0, 0, 0, 9, 9],
        [9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 0, 0, 0, 9, 9, 0, 0, 0, 9, 9],
        [9, 9, 9, 9, 0, 0, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

level_seven_hard_switches = np.array(
    [{"switch_location": (5, 12), "toggle_tiles": [(7, 6)]}]
)


# Level 8:
level_eight_env = np.array(
    [
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 5, 0, 9, 9, 9, 0, 0, 0, 0, 4, 0, 9, 9],
        [9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9, 9, 0, 0, 0, 0, 0, 0, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0, 0, 0, 9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    ]
)

level_eight_teleport_switches = np.array(
    [{"switch_location": (6, 7), "split_positions": [(3, 13), (9, 13)]}]
)
