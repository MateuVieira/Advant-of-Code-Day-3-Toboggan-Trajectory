import sys
from os import path, getcwd, system, name 
from time import perf_counter, sleep
from functools import reduce

def read_file(filename):
  try:
    with open(filename) as f:
        content = f.readlines()

    # I converted the file data to integers because I know 
    # that the input data is made up of numbers greater than 0
    content = [info.strip() for info in content]

  except:
    print('Error to read file')
    sys.exit()

  return content

def rotate(l, n):
  return l[n:] + l[:n]

def shift_data(data, right_number):
  for line, value in enumerate(data):
    data[line] = rotate(value, right_number)

  return data

def count_number_socks(data, right_number, down_number):
  count_of_socks = 0
  flag = True
  length_data = len(data) - 1
  line = 0

  while True:
    if (length_data == line) or (length_data < (line+down_number)) :
      break

    field = data[line+down_number][right_number]

    if field == '#':
      count_of_socks += 1

    data = shift_data(data, right_number)

    line += down_number

  return count_of_socks

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    rules = [
      {'Right': 1, 'Down': 1},
      {'Right': 3, 'Down': 1},
      {'Right': 5, 'Down': 1},
      {'Right': 7, 'Down': 1},
      {'Right': 1, 'Down': 2},
    ]

    for item in rules:
      data = input_data.copy()
      results.append(
        count_number_socks(
            data=data, 
            right_number=item.get('Right'),
            down_number=item.get('Down')
          )
      )

    result = reduce((lambda x, y: x * y), results)

    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)