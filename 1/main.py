def main():
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

if __name__ == "__main__":
  main()
