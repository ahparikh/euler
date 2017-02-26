def sum_divisble_by(number, maxval):
  n = maxval / number
  return number * (((n+1) * n) / 2)

def solution_sexy():
  print (sum_divisble_by(3, 999) + 
      sum_divisble_by(5, 999) - 
      sum_divisble_by(15, 999))

def solution_brute():
  tot = 0

  x = 3
  while x < 1000:
    tot += x
    x += 3

  x = 5
  while x < 1000:
    if x % 3 != 0:
      tot += x
    x += 5

  print tot

def main():
  solution_brute()
  solution_sexy()

if __name__ == "__main__":
  main()
