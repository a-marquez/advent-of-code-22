from collections import defaultdict
from functools import reduce
import operator
import sys

def visibility_north(grid, ri, ci):
  if ri == 0: return True
  tree_val = grid[ri][ci]
  trees_compare = [grid[yi][ci] for yi in range(0, ri)]
  return max(trees_compare) < tree_val

def visibility_south(grid, ri, ci):
  max_ri = len(grid) - 1
  if ri == max_ri: return True
  tree_val = grid[ri][ci]
  trees_compare = [grid[yi][ci] for yi in range(ri + 1, max_ri + 1)]
  return max(trees_compare) < tree_val

def visibility_west(grid, ri, ci):
  if ci == 0: return True
  tree_val = grid[ri][ci]
  trees_compare = [grid[ri][xi] for xi in range(0, ci)]
  return max(trees_compare) < tree_val

def visibility_east(grid, ri, ci):
  max_ci = len(grid[0]) - 1
  if ci == max_ci: return True
  tree_val = grid[ri][ci]
  trees_compare = [grid[ri][xi] for xi in range(ci + 1, max_ci + 1)]
  return max(trees_compare) < tree_val

if __name__ == '__main__':
  text_fname = sys.argv[0].split('.')[0] + '.txt'
  with open(text_fname) as file:
    content = file.read().strip()
    test_content = '''30373
25512
65332
33549
35390'''.strip()

    # trees = test_content.split('\n')
    trees = content.split('\n')

    trees = [*map(list, trees)]
    trees = [*map(lambda trow: [*map(int, trow)], trees)]
    trees_visible = defaultdict(dict)

    # print(trees, sep='\n')

    for ri, row in enumerate(trees):
      # print(ri, row)

      for ci, col in enumerate(trees[ri]):
        # print(ri, ci, col)
        # trees_visible[ri][ci] = visibility_north(trees, ri, ci)
        trees_visible[ri][ci] = any([visibility_north(trees, ri, ci),
          visibility_south(trees, ri, ci),
          visibility_west(trees, ri, ci),
          visibility_east(trees, ri, ci)])

    # for x in trees_visible: print(trees_visible[x].values())
    visibility_values = [*map(lambda tree_row: [*map(int, tree_row.values())], [*trees_visible.values()])]
    visibility_values = reduce(operator.add, visibility_values)
    visibility_values = reduce(operator.add, visibility_values)
    print(visibility_values)
