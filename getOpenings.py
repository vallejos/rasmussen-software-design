# filename getOpenings.py

# The getOpenings module accepts "openings" as an argument by reference and 
# gets the user input. This module is used by both getDoors and getWindows
# modules

def getOpenings(openings):
  openings = raw_input()
  openings = int(openings)

  return openings


# end module
