# filename displayCeilingResults.py

# The displayCeilingResults takes "area", "gallons" and "size" as parameters
# and displays the total ceiling area to paint for each ceiling as well as how
# many gallons are required for that painting. Finally, it displays the totals.

def displayCeilingResults(area, gallons, size):
  index = int(0)
  totalArea = float(0)
  totalGallons = float(0)
  
  for index in range(0, size):
    print "Total for Ceiling %d" % (index + 1)
    print "- Square feet to paint: %4.2f" % area[index]
    print "- Gallons of painting required: %4.2f" % gallons[index]
    
    totalArea += area[index]
    totalGallons += gallons[index]
  
  print "Total Ceiling's square feet to paint: %4.2f" % totalArea
  print "Total gallons of painting required: %4.2f" % totalGallons


# end module