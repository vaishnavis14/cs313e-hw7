#  File: Work.py

#  Description: The minimum lines that Vyaas codes before his first cup of coffee is returned through binary and linear search

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID: vs25229

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 09/28/2022

#  Date Last Modified: 09/28/2022

import sys, time

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:

  # an array is created with all the potential v values
  v_lines = []
  for i in range(1, n+1):
    v_lines.append(i)
  fewest_lines = 0

  # lines_code function determines how many lines are coded with each v value. The one with the fewest lines is returned
  for i in range(len(v_lines)):
    if lines_code(v_lines[i], n, k) >= n:
      fewest_lines = v_lines[i]
      break

  return fewest_lines

# The number of lines of coded is returned based on the v input
def lines_code(v, n, k):
  num_coffee = 0
  total_lines_code = 0
  # The loop continues until the total number of lines coded is less than or equal to n
  while total_lines_code <= n:
    num_lines = v //(k ** num_coffee)
    if num_lines <= 0:
      break
    else:
      total_lines_code += num_lines
      num_coffee += 1
  return total_lines_code

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # create list of all v values
  v_lines = []

  for i in range(1, n + 1):
    v_lines.append(i)

  # The high low and mid are determined
  high = len(v_lines) - 1
  low = 0
  mid = (high + low) // 2
  previous = 0
  found = False

  # low is changed if lines_code function is lower than n
  # high is changed if lines_code function is higher than n
  # if the function returns a number than is a repeat of the previous number or it equals n, the v value is returned
  while not found:
    if n == lines_code(v_lines[mid], n, k):
      return v_lines[mid]
    elif lines_code(v_lines[mid], n, k) == previous:
      return v_lines[mid]
    elif n > lines_code(v_lines[mid], n, k):
      low = mid + 1
    elif n < lines_code(v_lines[mid], n, k):
      high = mid
    previous = lines_code(v_lines[mid], n, k)
    mid = (high + low) // 2
# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()