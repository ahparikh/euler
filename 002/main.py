def fib():
  x = 0
  y = 1

  yield x
  yield y
  while True:
    x, y = y, x + y
    yield y

def main():
  fib_gen = fib()
  tot = 0
  for val in fib_gen:
    print val

    if val >= 4000000:
      break

    if val % 2 == 0:
      tot += val


  print "tot: ", tot

if __name__ == "__main__":
  main()
