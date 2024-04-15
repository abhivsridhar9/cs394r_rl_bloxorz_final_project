from levels.level import Level
from levels.env_config import *


l9 = Level(
    start_pos=(4, 4),
    base_env=level_nine_env,
    teleport_switches=level_nine_teleport_switches,
)

l9.reset()
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go down
l9.step(3)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go up
l9.step(1)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go down
l9.step(3)
print(l9.get_state())

# go left
l9.step(2)
print(l9.get_state())

# go left
l9.step(2)
print(l9.get_state())

# go left
l9.step(2)
print(l9.get_state())

# go left
l9.step(2)
print(l9.get_state())

# go left
l9.step(2)
print(l9.get_state())


# go up
l9.step(1)
print(l9.get_state())

# switch focus block
l9.step(4)
print(l9.get_state())

# go down
l9.step(3)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())
# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())

# go right
l9.step(0)
print(l9.get_state())


# go down
_, _, done = l9.step(3)
print(l9.get_state())
print(done)
