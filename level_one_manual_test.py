from levels.level import Level
from levels.env_config import *

l1 = Level(start_pos=(3, 6), base_env=level_one_env)
l1.reset()
print(l1.get_state())

# go right
l1.step(0)
print(l1.get_state())

# go right
l1.step(0)
print(l1.get_state())

# go down
l1.step(3)
print(l1.get_state())

# go right
l1.step(0)
print(l1.get_state())

# go right
l1.step(0)
print(l1.get_state())

# go right
l1.step(0)
print(l1.get_state())

# go down
_, _, done = l1.step(3)
print(l1.get_state())
print(done)