from collections import defaultdict
from math import trunc
import sys
if __name__ == '__main__':
  text_fname = sys.argv[0].split('.')[0] + '.txt'
  with open(text_fname) as file:
    content = file.read().strip()
    test_content = '''Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''.strip()

    # monkey_strings = content
    monkey_strings = test_content

    monkey_strings = monkey_strings.split('\n\n')

    monkeys = defaultdict(defaultdict)

    # get initial monkey_states
    for msi, ms in enumerate(monkey_strings):
      strings = ms.split('\n')
      monkeys[msi]['items'] = [*map(int, strings[1].split(': ')[1].split(', '))]
      monkeys[msi]['operation_string'] = compile(strings[2].split('= ')[1], '<string>', 'eval')
      monkeys[msi]['test_divisor'] = int(strings[3].split('by ')[1])
      monkeys[msi]['true_monkey'] = int(strings[4].split('monkey ')[1])
      monkeys[msi]['false_monkey'] = int(strings[5].split('monkey ')[1])
      monkeys[msi]['interactions'] = 0

    for r in range(0, 20):
    # for r in range(0, 1):
      for mi, m in enumerate(monkeys.values()):
        for ii in range(0, len(m['items'])):
          m['interactions'] += 1
          old = m['items'].pop(0)
          new = eval(m['operation_string'])
          new = trunc(new / 3)
          test = (new % m['test_divisor']) == 0
          # print(f'{mi} {old} {new} {test}')
          if test == True: monkeys[m['true_monkey']]['items'].append(new)
          else: monkeys[m['false_monkey']]['items'].append(new)

    interactions = []
    for m in monkeys.values(): interactions.append(m['interactions'])
    interactions.sort(reverse=True)
    for val in monkeys.values(): print(val)
    print(interactions[0] * interactions[1])

    monkeys2 = []

    # get initial monkey_states
    for msi, ms in enumerate(monkey_strings):
      strings = ms.split('\n')
      monkeys2.append([])
      monkeys2[msi].append([*map(int, strings[1].split(': ')[1].split(', '))])
      monkeys2[msi].append(compile(strings[2].split('= ')[1], '<string>', 'eval'))
      monkeys2[msi].append(int(strings[3].split('by ')[1]))
      monkeys2[msi].append(int(strings[4].split('monkey ')[1]))
      monkeys2[msi].append(int(strings[5].split('monkey ')[1]))
      monkeys2[msi].append(0)

    # for val in monkeys2: print(val)
    for r in range(0, 10000):
    # for r in range(0, 1):
      print(r)
      for m in monkeys2:
        for ii in range(0, len(m[0])):
          m[5] += 1
          old = m[0].pop(0)
          new = eval(m[1])
          test = (new % m[2]) == 0
          # print(f'{mi} {old} {new} {test}')
          if test == True: monkeys2[m[3]][0].append(new)
          else: monkeys2[m[4]][0].append(new)

    interactions2 = []
    for m in monkeys2: interactions2.append(m[5])
    interactions2.sort(reverse=True)
    for val in monkeys2: print(val)
    print(interactions2[0] * interactions2[1])
