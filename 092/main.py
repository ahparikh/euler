import pprint

def next_digit(number):
  # Quick on-liner to take a number, square each digit, sum them together
  # 145 -> 42
  return sum([int(digit)**2 for digit in str(number)])

def next_action(number, cache):
  # We skip the explicit check for 1 and 89 because we initialize the cache with
  # that.
  # Ret:
  #  - 1 or 89: this number hits 1 or 89
  #  - None: its not in cache, continue your chain
  return cache.get(number, None)

def update_cache(chain, end_number, cache):
  for i in chain:
    cache[i] = end_number

def main():
  # if we want to be cleaner, make a class that owns the chain cache and all the
  # number generation, next action, etc.
  # number -> 1 or 89
  chain_cache = {}
  chain_cache[1] = 1
  chain_cache[89] = 89

  cnt_89 = 0

  for i in range(1, 10000000):
    cur_chain = []
    nxt = i
    end_number = None

    # Simulate a do ... while
    while True:
      end_number = next_action(nxt, chain_cache)
      if end_number is not None:
        break
      else:
        cur_chain.append(nxt)
        nxt = next_digit(nxt)

    if 0 != len(cur_chain):
      update_cache(cur_chain, end_number, chain_cache)

    if 89 == end_number:
      cnt_89 += 1

  print cnt_89


if __name__ == "__main__":
  main()
