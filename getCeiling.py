# filename getCeiling.py

# The getCeiling module accepts "area" as an argument by reference, asks the 
# user if the ceiling is going to be included in the calculation, then if the
# ceiling is included, it asks for its dimensions and returns the calculated area.
# It sets the area to 0 if the ceiling is not included.

# import used modules
import validateQuestion
import getNumber

def getCeiling(area):
  # declare local variables
  ceiling = ""
  length = float(0)
  width = float(0)
  valid = False

  while (valid == False):
    # ask if ceiling must be included or not
    ceiling = raw_input("Include Ceiling (yes/no)?")
    
    valid = validateQuestion.validateQuestion(ceiling, valid)

    if (valid == False):
      print "ERROR: Please enter 'yes' or 'no'"

  if ceiling == "yes":
    # if ceiling is included, ask for its dimensions
    width = getNumber.getNumber("Width", width)
    width = float(width)

    length = getNumber.getNumber("Length", length)
    length = float(length)

    # calculates the area
    area = width * length
  else:
    area = float(0)

  return area

# end module
