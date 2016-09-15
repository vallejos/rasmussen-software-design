# filename validateNumber.py

# The validateNumber module takes "data" as an argument and "valid" as an 
# argument by reference. This modules validates if "data" is a positive number, 
# returning in "valid" the result.

def validateNumber(data, valid):
  
  if data > 0:
    valid = True
  else:
    valid = False

  return valid

#End module
