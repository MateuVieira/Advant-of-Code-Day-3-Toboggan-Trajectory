import sys
from os import path, getcwd, system, name 
from time import perf_counter, sleep

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

def shift_data(data):
  for line, value in enumerate(data):
    data[line] = rotate(value, 3)

  return data

def count_number_socks(data):
  count_of_socks = 0
  flag = True
  length_data = len(data) - 1

  for line, value in enumerate(data):
    if length_data == line:
      break

    field = data[line+1][3]

    if field == '#':
      count_of_socks += 1

    data = shift_data(data)

  return count_of_socks

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'inputData.txt')
    input_data = read_file(filename)

    result = count_number_socks(data=input_data)

    print(f'Result: {result}')

    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')
    print('End of script')
    sys.exit(0)