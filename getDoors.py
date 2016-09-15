# filename getDoors.py

# The getDoors module accepts "doors" as an argument by reference and returns
# the number of doors included in the room. A door has a constant size.

# import used modules
import getOpenings

def getDoors(doors):
  print("Enter number of doors in the room: ")
  doors = getOpenings.getOpenings(doors)

  return doors


# end module
