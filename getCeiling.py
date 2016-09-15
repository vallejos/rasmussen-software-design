# filename getCeiling.py

# The getRoomArea module accepts "area" as an argument by reference,
# asks the user to input the height, length and width of the room and returns
# the resulting calculated area. Assumes a square or rectangular room.

def getCeiling(area):
  ceiling = ""
  length = float(0)
  width = float(0)

  # ask if ceiling must be included or not
  ceiling = raw_input("Include Ceiling (yes/no)?")

  if ceiling == "yes":
    # if ceiling is included, ask for its dimensions
    width = raw_input("- Enter Width: ")
    width = float(width)

    length = raw_input("- Enter Length: ")
    length = float(length)

    # calculates the area
    area = width * length
  else:
    area = float(0)

  return area


# end module
