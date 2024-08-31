
data_structure = [
  [1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}),
  "Hello",  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure(*args):
  sum = 0
  for i in args:
    if isinstance(i, list):
      for elem in i:
        sum += calculate_structure(elem)
    elif isinstance(i, set):
      for elem in i:
        sum += calculate_structure(elem)
    elif isinstance(i, tuple):
      for elem in i:
        sum += calculate_structure(elem)
    elif isinstance(i, dict):
      for key, value in i.items():
        sum += calculate_structure(key, value)
    elif isinstance(i, str):
        sum += len(i)
    elif isinstance(i, int):
        sum += i
  return sum



result = calculate_structure(data_structure)
print(result)

