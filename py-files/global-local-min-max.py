def global_max_min(coords):
  global_max = -float('inf')
  global_min = float('inf')

  for coord in coords:
    if coord['y'] > global_max:
      global_max = coord['y']
    if coord['y'] < global_min:
      global_min = coord['y']
  
  return (global_max, global_min)

# Example usage
coords = [{'x': -1, 'y': 7}, {'x': 0, 'y': 0}, {'x': 1, 'y': -1}, {'x': 2, 'y': 16}]
global_max, global_min = global_max_min(coords)
print(f"Global maximum: {global_max}")
print(f"Global minimum: {global_min}")


def find_local_extrema(coords):
  extrema = []
  for i in range(1, len(coords)-1):
    # Check if this is a local maximum
    if coords[i-1]['y'] < coords[i]['y'] and coords[i+1]['y'] < coords[i]['y']:
      extrema.append({'x': coords[i]['x'], 'y': coords[i]['y'], 'type': 'local maximum'})
    # Check if this is a local minimum
    elif coords[i-1]['y'] > coords[i]['y'] and coords[i+1]['y'] > coords[i]['y']:
      extrema.append({'x': coords[i]['x'], 'y': coords[i]['y'], 'type': 'local minimum'})
  return extrema

coords = [{'x': -1, 'y': 7}, {'x': 0, 'y': 0}, {'x': 1, 'y': -1}, {'x': 2, 'y': 16}]
local_extrema = find_local_extrema(coords)
for extrema in local_extrema:
  print(f"{extrema['type']}: ({extrema['x']}, {extrema['y']})")