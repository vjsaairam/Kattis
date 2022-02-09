line = input()
data_set = []
result = ''

def compute_miles(data_set):
  sum_of_prev_time_values = 0
  total_miles = 0

  for value in data_set:
    spped_and_time = value.split(' ')
    speed = int(spped_and_time.pop(0))
    time = int(spped_and_time.pop(0)) - sum_of_prev_time_values
    sum_of_prev_time_values += time
    total_miles += speed * time
  return total_miles

while line != '-1':
  line = input()
  if line.find(' ') == -1:
    if len(data_set) > 0:
      result += str(compute_miles(data_set)) + ' miles\n'
    else:
      result += ''
    data_set = []
  else:
    data_set.append(line)


print(result)
