# filename calculateGallons.py

# The calculateGallons module takes "area" as an argument and "gallons" as an 
# argument by reference to calculate how many gallons are required to cover
# the area passed as a parameter. It uses the  SQ_FEET_PER_GALLON constant and 
# a simple relation formula to set gallons.

# import required global constant
from main import SQ_FEET_PER_GALLON

def calculateGallons(gallons, area):
  global SQ_FEET_PER_GALLON
  
  gallons = area / SQ_FEET_PER_GALLON

  return gallons


# end module
