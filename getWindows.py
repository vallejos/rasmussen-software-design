# filename getWindows.py

# The getWindows module accepts "windows" as an argument by reference and returns
# the number of windows included in the room. A window has a constant size.

# import used modules
import getOpenings

def getWindows(windows):
  print("Enter number of windows in the room: ")
  windows = getOpenings.getOpenings(windows)

  return windows


# end module
