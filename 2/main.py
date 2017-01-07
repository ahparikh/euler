def next_fib():
  x = 0
  y = 1

  yield x
  yield y
  while True:
    x, y = y, x + y
    yield y

def main():
  tot = 0
  for val in next_fib():
    if val >= 100:
      break

    if val % 2 == 0:
      tot += val

    val = next_fib()
    print val

  print tot

if __name__ == "__main__":
  main()
