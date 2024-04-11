from levels.level import Level
from levels.env_config import *


l8 = Level(
    start_pos=(6, 3),
    base_env=level_two_env,
    circle_switches=level_two_circle_switches,
    x_switches=level_two_x_switches,
)
l8.reset()
print(l8.get_state())

# go up
l8.step(1)
print(l8.get_state())

# go right
l8.step(0)
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

# go right
l8.step(0)
print(l8.get_state())

# go up
l8.step(1)
print(l8.get_state())

# go up
l8.step(1)
print(l8.get_state())

# go up
l8.step(1)
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

# go right
l8.step(0)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go right
l8.step(0)
print(l8.get_state())

# go up
l8.step(1)
print(l8.get_state())

# go left
l8.step(2)
print(l8.get_state())


# go up
_, _, done = l8.step(1)
print(l8.get_state())
print(done)
