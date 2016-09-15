# filename swap.py

# This module takes two arguments "i" and "j" by reference and swaps them.
# The value of "j" is returned on "i" and the "i" value is returned in "j".
# It uses a temporary variable not to overwrite or lose any data

def swap(i, j):
  # declare local variables
  temp = i
  i = j
  j = temp

  return (i, j)

# end module
