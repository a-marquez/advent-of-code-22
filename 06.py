if __name__ == '__main__':
  with open('input.txt') as file:
    content = file.read().strip()
    test_content = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

    signal = content
    # signal = test_content

    print(signal)
    packet_start_index = 0
    for i, char in [*enumerate(signal)][:-3]:
      chunk = signal[i: i+4]
      repeats = any([*map(lambda c: chunk.count(c) > 1, chunk)])
      # print(f'Index:{i} Char:{char} Repeats:{repeats} Chunk:{chunk}')
      if repeats == False:
        packet_start_index = i
        break
    print(len(signal[:packet_start_index + 4]))

    message_start_index = 0
    for i, char in [*enumerate(signal)][:-13]:
      chunk = signal[i: i+14]
      repeats = any([*map(lambda c: chunk.count(c) > 1, chunk)])
      # print(f'Index:{i} Char:{char} Repeats:{repeats} Chunk:{chunk}')
      if repeats == False:
        message_start_index = i
        break

    print(len(signal[:message_start_index + 14]))
