from collections import defaultdict
import functools
import operator

if __name__ == '__main__':
  with open('05.txt') as file:

    test_input = '''    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    '''


    instructions = file.read().strip()
    # instructions = test_input

    crates_str, movements = instructions.split('\n\n')
    movements = movements.strip()
    crates_str = crates_str.split('\n')[:-1]
    crates_str.reverse()

    stacks = defaultdict(list)

    stacks_2 = defaultdict(list)

    for row in crates_str:
      col_count = int((len(row) + 1) / 4) - 1
      # print(row, len(row), col_count)
      for col_i in range(0, col_count + 1):
        char_index = -3 + 4 * (col_i + 1)
        # print(char_index)
        char = row[char_index]
        if char != ' ':
          stacks[col_i].append(char)
          stacks_2[col_i].append(char)

    print(stacks)

    for text in movements.split('\n'):
      text_parts = text.split(' ')
      move_length = int(text_parts[1])
      stack_start_index = int(text_parts[3]) - 1
      stack_end_index = int(text_parts[5]) - 1

      for i in range(move_length):
        # print(f'{i} {stack_start_index} -> {stack_end_index}')
        stacks[stack_end_index].append(stacks[stack_start_index].pop())

      # print(f'{stack_start_index} {stack_end_index} {move_length} {stacks_2[stack_start_index][:-move_length]}')
      stacks_2[stack_end_index] += stacks_2[stack_start_index][-move_length:]
      del stacks_2[stack_start_index][-move_length:]

    print(stacks)

    stack_values = [*stacks.values()]
    ending_stack_values = functools.reduce(operator.add, [*map(lambda list: list[-1], stack_values)])
    print(ending_stack_values)

    print(stacks_2)

    stack_2_values = [*stacks_2.values()]
    ending_stack_2_values = functools.reduce(operator.add, [*map(lambda list: list[-1], stack_2_values)])
    print(ending_stack_2_values)




