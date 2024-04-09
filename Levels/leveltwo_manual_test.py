from levels.leveltwo import LevelTwo

l2 = LevelTwo()
l2.reset()
print(l2.get_state())

# go up
l2.step(1)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go down
l2.step(3)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go up
l2.step(1)
print(l2.get_state())

# go up
l2.step(1)
print(l2.get_state())

# go up
l2.step(1)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go down
l2.step(3)
print(l2.get_state())

# go down
l2.step(3)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go right
l2.step(0)
print(l2.get_state())

# go up
l2.step(1)
print(l2.get_state())

# go left
l2.step(2)
print(l2.get_state())


# go up
_, _, done = l2.step(1)
print(l2.get_state())
print(done)
