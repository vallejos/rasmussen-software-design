# filename getNumber.py

# The getNumber module takes "name" as an argument, and "value" as an 
# argument by reference. It asks for the input until a valid value is entered,
# and returns the entered value in the "value" argument.

# import used modules
import validateNumber

def getNumber(name, value):
  # define local variables
  valid = False

  # repeat until a valid number is entered
  while (valid == False):
    # ask for number
    print "- Enter %s: " % name
    value = raw_input()
    value = float(value)
    
    valid = validateNumber.validateNumber(value, valid)

    if (valid == False):
      print "ERROR: %s cannot be equal to or less than zero." % name

  return value

# end module
    