###------------------------------------------------------
### Course Project, by Leonardo Vallejos
###------------------------------------------------------
### This program calculates the area of a room in order to purchase cans of paint.
###
### Some global constants are used based on the references found at 
### http://www.sherwin-williams.com/homeowners/color/color-selection-tools/paint-calculator/ 
###------------------------------------------------------

### Begin main module

# Import used modules
import getDoors
import getCeiling
import getRoomArea
import getWindows
import getOpenings
import calculateGallons
import displayCeilingResults
import displayWallResults
import validateQuestion
import validateNumber
import getNumber
import swap

# Declare some global constants
global DOOR_AREA, WINDOW_AREA, SQ_FEET_PER_GALLON
DOOR_AREA = int(21)              # assumes 3' x 7' doors
WINDOW_AREA = int(15)            # assumes 3' x 5' windows
SQ_FEET_PER_GALLON = int(400)    # For one coat of painting, one gallon will cover 400 square feet

def main():
  # Declare local variables
  wallArea = float(0)
  ceilingArea = float(0)
  doorsArea = float(0)
  windowsArea = float(0)
  wallGallons = float(0)
  ceilingGallons = float(0)
  doors = int(0)
  windows = int(0)
  size = int(0)
  index = int(0)
  areasWall = []
  areasCeiling = []
  gallonsWall = []
  gallonsCeiling = []
  
  size = raw_input("Enter number of rooms to paint: ")
  size = int(size)

  for index in range(0, size):
    # Get room dimensions
    wallArea = getRoomArea.getRoomArea(wallArea)

    # Get number of doors
    doors = getDoors.getDoors(doors)
    doorsArea = doors * DOOR_AREA

    # Get number of windows
    windows = getWindows.getWindows(windows)
    windowsArea = windows * WINDOW_AREA

    # Recalculates area to consider windows and doors
    wallArea = wallArea - doorsArea - windowsArea

    # Include ceiling?
    ceilingArea = getCeiling.getCeiling(ceilingArea)

    # Calculate gallons required to paint the wall
    wallGallons = calculateGallons.calculateGallons(wallGallons, wallArea)

    # Calculate gallons required to paint the ceiling
    ceilingGallons = calculateGallons.calculateGallons(ceilingGallons, ceilingArea)
    
    areasWall.append(wallArea)
    areasCeiling.append(ceilingArea)
    gallonsWall.append(wallGallons)
    gallonsCeiling.append(ceilingGallons)
    
  # Display the results
  displayWallResults.displayWallResults(areasWall, gallonsWall, size)
  displayCeilingResults.displayCeilingResults(areasCeiling, gallonsCeiling, size)

# invoke main module when called from the terminal
if __name__ == "__main__":
    main()

### End main module
