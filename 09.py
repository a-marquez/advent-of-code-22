import sys
from functools import reduce
import operator
if __name__ == '__main__':
  text_fname = sys.argv[0].split('.')[0] + '.txt'
  with open(text_fname) as file:
    content = file.read().strip()
    test_content = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''.strip()

    steps = content
    # steps = test_content

    steps = [*map(lambda row: (row.split(' ')[0], int(row.split(' ')[1])), steps.split('\n'))]
    steps = [*map(lambda step_pair: list(step_pair[0] * step_pair[1] ), steps)]
    steps = reduce(operator.add, steps)

    direction_fn_dict = {
      'U': lambda pos: [pos[0], pos[1] + 1],
      'D': lambda pos: [pos[0], pos[1] - 1],
      'R': lambda pos: [pos[0] + 1, pos[1]],
      'L': lambda pos: [pos[0] - 1, pos[1]]
    }

    greater_than_1 = lambda d: d > 1
    any_greater_than_1 = lambda pair: any([*map(greater_than_1, pair)])
    equals_2_1_pair = lambda pair: 2 in pair and 1 in pair

    clamp_step_range = lambda n: max(-1, min(n, 1))

    tail_locations_unique = {(0, 0)}
    tail_location = [0, 0]
    head_location = [0, 0]

    print(f'Initial head_location: {head_location}')
    for si, direction in enumerate(steps):
      head_location = direction_fn_dict[direction](head_location)
      x_pairs = [head_location[0], tail_location[0]]
      y_pairs = [head_location[1], tail_location[1]]
      distances = [max(x_pairs) - min(x_pairs), max(y_pairs) - min(y_pairs)]
      is_separated = any_greater_than_1(distances)
      is_separated_diagonally = equals_2_1_pair(distances)

      # print(f'{direction} h: {head_location}, t: {tail_location} d: {distances} sep?: {is_separated} sep_diag?: {is_separated_diagonally}')

      if is_separated:
        deltas = [head_location[0] - tail_location[0], head_location[1] - tail_location[1]]
        tail_step_delta = [*map(clamp_step_range, deltas)]
        tail_location[0] = tail_location[0] + tail_step_delta[0]
        tail_location[1] = tail_location[1] + tail_step_delta[1]

      tail_locations_unique.add(tuple(tail_location))
    print(len(tail_locations_unique))

    last_knot_locations_unique = {(0, 0)}
    knot_locations  = [[0, 0]] * 10

    def get_next_knot_location(lead_knot, follow_knot):
      x_pairs = [lead_knot[0], follow_knot[0]]
      y_pairs = [lead_knot[1], follow_knot[1]]
      distances = [max(x_pairs) - min(x_pairs), max(y_pairs) - min(y_pairs)]
      is_separated = any_greater_than_1(distances)
      next_knot_location = follow_knot[:]
      if is_separated:
        deltas = [lead_knot[0] - follow_knot[0], lead_knot[1] - follow_knot[1]]
        follow_step_delta = [*map(clamp_step_range, deltas)]
        next_knot_location[0] = follow_knot[0] + follow_step_delta[0]
        next_knot_location[1] = follow_knot[1] + follow_step_delta[1]
      return next_knot_location

    for direction in steps:
      for ki, knot in enumerate(knot_locations):
        if ki == 0:
          knot_locations[0] = direction_fn_dict[direction](knot_locations[0])
        else:
          knot_locations[ki] = get_next_knot_location(knot_locations[ki - 1], knot_locations[ki])
        if ki == len(knot_locations) - 1:
          last_knot_locations_unique.add(tuple(knot_locations[ki]))

    print(knot_locations)
    print(len(last_knot_locations_unique))

