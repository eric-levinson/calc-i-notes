# From the graph of the velocity, determine the distance from the area between the graph and the horizontal axis.
import math

cords = [(0, 0), (1, 1), (2, 1), (3, 3), (4, 3), (5, 0)]

def distance(cord1, cord2):
  """Calculates the distance between two cord objects"""
  x1, y1 = cord1
  x2, y2 = cord2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(cords, interval):
  """Calculates the total distance traveled on a given interval"""
  start, end = interval
  distance_traveled = 0
  for i in range(start, end):
    distance_traveled += distance(cords[i], cords[i+1])
  return distance_traveled

# Calculate the total distance traveled on the interval [1, 5]
interval = (1, 5)
total_distance_traveled = total_distance(cords, interval)
print(f"Total distance traveled on interval {interval}: {total_distance_traveled}")
