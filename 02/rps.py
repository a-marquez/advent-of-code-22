import functools
import operator

value_range = [1, 2, 3]

hand_values = {
  'A': 1, # rock
  'B': 2, # paper
  'C': 3, # scissors
  'X': 1, # ...
  'Y': 2,
  'Z': 3,
}

hand_labels = {
  'A': 'rock    ', # rock
  'B': 'paper   ', # paper
  'C': 'scissors', # scissors
  'X': 'rock    ', # ...
  'Y': 'paper   ',
  'Z': 'scissors',
}

def values_to_p1_outcome(value_pair):
  p2, p1 = value_pair
  if p1 == p2: # draw
    return p1 + 3
  elif (p1 == 1 and p2 == 3) or (p1 == 2 and p2 ==1) or (p1 == 3 and p2 == 2): # loss
    return p1 + 6
  else: # win
    return p1

def hand_pairs_to_values(hand_pairs):
  values = [*map(lambda hand: hand_values[hand], hand_pairs.split(' '))]
  return values

def hand_pairs_to_labels(hand_pairs):
  values = [*map(lambda hand: hand_labels[hand], hand_pairs.split(' '))]
  return values

if __name__ == '__main__':
  with open('input.txt') as input_file:
    input_content = input_file.read().strip().split('\n')
    value_pairs = [*map(hand_pairs_to_values, input_content)]
    label_pairs = [*map(hand_pairs_to_labels, input_content)]
    p1_scores = [values_to_p1_outcome(pair) for pair in value_pairs]
    p1_score = functools.reduce(operator.add, p1_scores)
    print(p1_score)

    total_score = 0
    for i, pair in enumerate(value_pairs):
      p2 = pair[0]
      outcome = input_content[i].split(' ')[1]
      score = 0
      if outcome == 'Y': # draw
        score = 3 + p2
      elif outcome == 'X': # loss
        p1 = value_range[((p2 -1) + 2) % len(value_range)]
        score = p1
      elif outcome == 'Z': # loss
        p1 = value_range[((p2 -1) + 1) % len(value_range)]
        score = 6 + p1
      # print(f'{p2} {outcome} {score}')
      total_score += score
    print(total_score)
