from levels.level import Level
from levels.env_config import *


l8 = Level(
    start_pos=(6, 4),
    base_env=level_eight_env,
    teleport_switches=level_eight_teleport_switches,
)
l8.reset()
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go down
l8.step(3)
print(l8.get_state())

# go down
l8.step(3)
print(l8.get_state())

# go down
l8.step(3)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# switch focus block
l8.step(4)
print(l8.get_state())

# go up
l8.step(1)
print(l8.get_state())
print(l8.get_block().get_focus())

# go up
l8.step(1)
print(l8.get_state())
print(l8.get_block().get_focus())

# go up
l8.step(1)
print(l8.get_state())
print(l8.get_block().get_focus())

# go right
l8.step(0)
print(l8.get_state())

# go right
_, _, done = l8.step(0)
print(l8.get_state())
print(done)
# # go right
# l8.step(0)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())


# # go up
# l8.step(1)
# print(l8.get_state())

# # go up
# l8.step(1)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go down
# l8.step(3)
# print(l8.get_state())

# # go down
# l8.step(3)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go right
# l8.step(0)
# print(l8.get_state())

# # go up
# l8.step(1)
# print(l8.get_state())

# # go left
# l8.step(2)
# print(l8.get_state())


# # go up


