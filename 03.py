import functools
import operator
from itertools import islice

#https://stackoverflow.com/questions/312443/how-do-i-split-a-list-into-equally-sized-chunks
def chunk(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

if __name__ == '__main__':
  test_rucksacks = '''
  vJrwpWtwJgWrhcsFMMfFFhFp
  jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
  PmmdzqPrVvPwwTWBwg
  wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
  ttgJtRGJQctTZtZT
  CrZsJsPPZsGzwwsLwLmpwMDw
  '''

  char_codes = [x for x in range(ord('a'), ord('z') + 1)] + [x for x in range(ord('A'), ord('Z') + 1)]
  chars = [*map(chr, char_codes)]
  char_value_dict = {char: i + 1 for i, char in enumerate(chars)}
  # print(char_value_dict)

  with open('03.txt') as file:
    # rucksacks = test_rucksacks
    rucksacks = file.read()
    items = [*map(lambda string: string.strip(), rucksacks.strip().split('\n'))]
    item_pairs = [*map(lambda pair: [[*pair[:len(pair)//2]], pair[len(pair)//2:]], items)]
    duplicate_items_unique = [*map(lambda pair: [*{x for x in pair[0] if x in pair[1]}][0], item_pairs)] # set comprehension instead of list comprehension, curly braces
    item_values = [*map(lambda char: char_value_dict[char], duplicate_items_unique)]
    item_sum = functools.reduce(operator.add, item_values)

    # print(items, item_pairs, duplicate_items_unique, item_values, sep='\n\n')
    print(item_sum)

    grouped_items = list(chunk(items, 3))
    flat_group_items_unique = [*map(lambda item_group: [*{x for x in functools.reduce(operator.iconcat, item_group)}], grouped_items)]
    matching_group_items = []

    for i, unique_group_items in enumerate(flat_group_items_unique):
      matching_group_items.append(*filter(lambda item: item in grouped_items[i][0] and item in grouped_items[i][1] and item in grouped_items[i][2] , unique_group_items))
      # print(grouped_items[i], unique_group_items)

    group_item_values = [*map(lambda char: char_value_dict[char], matching_group_items)]
    group_item_sum = functools.reduce(operator.add, group_item_values)

    # print(grouped_items, flat_group_items_unique, matching_group_items, sep='\n\n')
    print(group_item_sum)
