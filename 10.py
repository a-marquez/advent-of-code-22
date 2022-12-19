import sys
if __name__ == '__main__':
  text_fname = sys.argv[0].split('.')[0] + '.txt'
  with open(text_fname) as file:
    content = file.read().strip()
    test_content = '''noop
addx 3
addx -5'''.strip()
    test_content2 = '''addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
'''.strip()

  instructions = content
  # instructions = test_content
  # instructions = test_content2

  instructions = instructions.split('\n')

  X = 1

  cycle_values = [1]

  for instruction in instructions:
    if instruction == 'noop':
      cycle_values.append(X)
    else:
      add_value = int(instruction.split(' ')[1])
      cycle_values.append(X + 0)
      cycle_values.append(X + add_value)
      X += add_value

  signal_sums = 0
  for i in [19, 59, 99, 139, 179, 219]:
    signal_sums += (cycle_values[i] * (i + 1))
    print(i + 1, cycle_values[i], cycle_values[i] * (i + 1), signal_sums)

  print(cycle_values)
  print(signal_sums)


  for ir in range(1, 7):
    # print (((ir - 1) * 40), 40 * ir)
    row = []
    for i in range(((ir - 1) * 40), 40 * ir):
      # print(i)
      middle = cycle_values[i]
      sprite_values = [middle - 1, middle, middle + 1]
      if ((i) - ((ir - 1) * 40)) in sprite_values: row.append('#')
      else: row.append('.')
    print(''.join(row))




