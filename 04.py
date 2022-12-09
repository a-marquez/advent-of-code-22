# add one to range end for actual intended range, otherwise one short
section_to_range = lambda section_str: [*range(int(section_str.split('-')[0]), int(section_str.split('-')[1]) + 1)]

if __name__ == '__main__':
  with open('04.txt') as file:
    test_data = '''
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    '''

    # elf_pairs = test_data.strip().split('\n')
    elf_pairs = file.read().strip().split('\n')

    overlapping_pairs_complete = 0
    overlapping_pairs_any = 0

    for p in elf_pairs:
      section_1_str, section_2_str = p.strip().split(',')
      section_1_range = section_to_range(section_1_str)
      section_2_range = section_to_range(section_2_str)
      if (all(item in section_1_range for item in section_2_range) or all(item in section_2_range for item in section_1_range)):
        overlapping_pairs_complete += 1
      if (any(item in section_1_range for item in section_2_range)):
        overlapping_pairs_any += 1

    print(f'overlapping_pairs_complete = {overlapping_pairs_complete}')
    print(f'overlapping_pairs_any = {overlapping_pairs_any}')






