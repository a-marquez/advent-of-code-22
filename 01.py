import functools

def sum(a, b):
  return a + b

def cals_to_sums(cal_string):
  return functools.reduce(
    sum,
    [*map(int, cal_string.split('\n'))]
  )

if __name__ == '__main__':
  with open('01.txt') as input_file:
    input_content = input_file.read().strip()
    elf_calories = input_content.split('\n\n')
    elf_calories = [*map(cals_to_sums, elf_calories)]
    max_calories = max(elf_calories)
    print(f'max_calories: {max_calories}')

    elf_calories.sort()
    top_3_calories = functools.reduce(sum, elf_calories[-3:])
    print(f'top_3_calories: {top_3_calories}')
