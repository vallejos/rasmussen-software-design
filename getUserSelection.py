# filename getUserSelection.py

# The getUserSelection module will get the user menu selection and return it 
# in the parameter. It takes "menuSelection" as a parameter by reference.

def getUserSelection(menuSelection):
  print "- Enter your selection"
  menuSelection = raw_input()
  value = int(menuSelection)

  return value

# end module
    