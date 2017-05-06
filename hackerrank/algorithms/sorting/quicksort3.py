#!/usr/bin/env python2

TEST_MODE = False

def main():
  length = int(raw_input().strip())
  array = map(int, raw_input().strip().split())
  quicksort(array, 0, len(array)-1)

def quicksort(array, low, high):
  if low < high:
    array, p = partition(array, low, high)
    return quicksort(quicksort(array, low, p - 1), p + 1, high)
  else:
    return array

def partition(array, low, high):
  pivot = array[high]
  i = low
  for j in range(low, high):
    if array[j] <= pivot:
      array[i], array[j] = array[j], array[i]
      i += 1
  array[i], array[high] = array[high], array[i]
  print ' '.join(map(str, array))
  return array, i

def quicksort_old(array):
  if len(array) > 1:
    equal, left, right = [array[0]], [], []
    for i in range(1, len(array)):
      if array[i] < equal[0]:
        left.append(array[i])
      elif array[i] > equal[0]:
        right.append(array[i])
      else:
        equal.append(array[i])
    output = quicksort(left) + equal + quicksort(right)
    print ' '.join(map(str, output))
    return output
  else:
    return array

def test():
#  print quicksort([-13, 68, -43, -71, -39, -10, 40, -49, -19, -3, -70, -62, -76, -94, -73, 64, 72, -5, 88, 2, -63, 92, -40, 16, 49, 47, -86, -51, -9, -14, 96, 74, -22, -34, 38, -12, 6, 63, 19, -69, 14, -90, -27, 76, 54, 57, -87, -91, 43, -92])
#  print quicksort([4, 4, 4, 4, 4])
#  print quicksort([3, 4, 5, 6, 7])
#  print quicksort([7, 6, 5, 4, 3])
#  print quicksort([-7, 6, -8, 4, 5])
#  print quicksort([-7, 6, -8, -8, 5])
#  print quicksort([-7, -7, -7, -7, -7])
#  print quicksort([0, -3, 6, 4, -10, 8, -5, 2, -7])
#  print quicksort([9, 0, -3, 6, 4, -10, 8, -5, 2, -7])
#  array = [5, 8, 1, 3, 7, 9, 2]
  array = [1, 3, 9, 8, 2, 7, 5]
  quicksort(array, 0, len(array)-1)

test() if TEST_MODE else main()
