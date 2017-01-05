def next_digit(number):
  return sum([int(digit)**2 for digit in str(number)])

def test(number, number_chains):
  if number in number_chains:
    return None

  return next_digit(number)

def update_chains(chain, next, number_chains):
  for i in range(len(chain) - 1):
    number_chains[chain[i]] = (chain[i+1], next)

def main():
  number_chains = {}

  for i in range(1, 100):
    if i in number_chains:
      continue

    chain = []
    next = i

    while next is not None:
      chain.append(next)
      next = test(next, number_chains)

      if 1 == next or 89 == next:
        break

    update_chains(chain, next, number_chains)

  print number_chains

if __name__ == "__main__":
  main()
