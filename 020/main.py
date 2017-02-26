import math

def main():
  sum = 0
  for letter in str(math.factorial(100)):
    sum += int(letter)

  print sum
  

if __name__ == "__main__":
      main()
