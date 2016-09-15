# filename getDoors.py

# The getRoomArea module accepts "area" as an argument by reference,
# asks the user to input the height, length and width of the room and returns
# the resulting calculated area. Assumes a square or rectangular room.

def getRoomArea(area):
  height = float(0)
  length = float(0)
  width = float(0)
  
  print("Enter dimensions for the room")

  # ask for room's width
  width = raw_input("- Enter Width: ")
  width = float(width)

  # ask for room's length
  length = raw_input("- Enter Length: ")
  length = float(length)

  # ask for room's height
  height = raw_input("- Enter Height: ")
  height = float(height)

  # calculates the area
  area = 2 * (height * length) + 2 * (width * length)

  return area


# end module
