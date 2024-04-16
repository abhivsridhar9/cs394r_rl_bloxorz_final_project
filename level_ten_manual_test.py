from levels.level import Level
from levels.env_config import *


l10 = Level(
    start_pos=(2, 12),
    base_env=level_ten_env,
    soft_switches=level_ten_soft_switches,
    hard_switches=level_ten_hard_switches,
    teleport_switches=level_ten_teleport_switches,
)

l10.reset()
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())


# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# switch focus block
l10.step(4)
print(l10.get_state())


# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go down
l10.step(3)
print(l10.get_state())


# go up
l10.step(1)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go up
l10.step(1)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# switch focus block
l10.step(4)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go right
l10.step(0)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
l10.step(2)
print(l10.get_state())

# go left
_, _, done = l10.step(2)
print(l10.get_state())
print(done)
