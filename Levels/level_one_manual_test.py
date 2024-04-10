from Levels.levelone import LevelOne

l1 = LevelOne()
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
