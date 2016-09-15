# filename getDoors.py

# The getRoomArea module accepts "area" as an argument by reference,
# asks the user to input the height, length and width of the room and returns
# the resulting calculated area. Assumes a square or rectangular room.

# import used modules
import getNumber

def getRoomArea(area):
  height = float(0)
  length = float(0)
  width = float(0)
  
  print("Enter dimensions for the room")

  # ask for room's width
  width = getNumber.getNumber("Width", width)
  width = float(width)

  # ask for room's length
  length = getNumber.getNumber("Length", length)
  length = float(length)

  # ask for room's height
  height = getNumber.getNumber("Height", height)
  height = float(height)

  # calculates the area
  area = 2 * (height * length) + 2 * (width * length)

  return area


# end module
