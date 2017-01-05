def main():
  sum = 0
  for letter in str(2**1000):
    sum += int(letter)

  print sum

if __name__ == "__main__":
      main()
