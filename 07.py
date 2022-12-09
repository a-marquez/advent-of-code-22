from functools import reduce
from collections import defaultdict
import operator

import pprint

def dictByPath(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

if __name__ == '__main__':
  with open('input.txt') as file:
    content = file.read().strip()
    test_content = '''$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k'''.strip()

    # terminal_view = test_content
    terminal_view = content

    def rec_dd():
      return defaultdict(rec_dd, _size=0)
    dir_tree = rec_dd()

    pwd = []

    terminal_chunks = filter(lambda chunk: chunk != '', terminal_view.split('$ '))

    paths_set = []

    # create dict tree
    for i, c in enumerate(terminal_chunks):
      lines = [*filter(lambda chunk: chunk != '', c.split('\n'))]
      command = lines[0]
      output = lines[1:]
      files = [*filter(lambda line: not line.startswith('dir '), output)]
      print(i, command, files, pwd)
      if command.startswith('cd') and command.endswith('..'):
        pwd.pop()
      elif command.startswith('cd'):
        pwd.append(command.split(' ')[1])
      elif command.startswith('ls'):
        for f in files:
          f_size, name = f.split(' ')
          f_size = int(f_size)
          dictByPath(dir_tree, pwd)[name] = f_size
          # increment parent dir sizes
          for i in [*range(1, len(pwd) + 1)]:
            print(i, pwd[: i])
            dictByPath(dir_tree, pwd[: i])['_size'] += f_size

      if pwd[:] not in paths_set: paths_set.append(pwd[:])


    dir_sizes = [*map(lambda path: dictByPath(dir_tree, path)['_size'], paths_set)]
    sizes_under_100k = [*filter(lambda size: size <= 100000, dir_sizes)]
    sum_sizes_under_100k = reduce(operator.add, sizes_under_100k)


    pp = pprint.PrettyPrinter(depth=4)
    pp.pprint(dir_tree)
    # print(paths_set, dir_sizes, sizes_under_100k, sep='\n')
    print(paths_set, dir_sizes, sizes_under_100k, sum_sizes_under_100k, sep='\n')

    # second half
    print('---')
    unused_space = 70000000 - dir_tree['/']['_size']
    req_min_space = 30000000
    min_del_space = req_min_space - unused_space
    dir_sizes.sort()
    print(unused_space, min_del_space, [*filter(lambda n: n >= min_del_space, dir_sizes)][0], sep='\n')
