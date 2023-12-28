enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# Global Scope
# There is no Block Scope
# GLOBAL Constants

