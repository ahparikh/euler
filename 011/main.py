import pprint

def findMaxProduct(grid):
  maxProd = 0
  num_rows = len(grid)
  num_cols = len(grid[0])

  for row in range(num_rows):
    for col in range(num_cols):
      # row prod
      if row + 3 < num_rows:
        row_prod = prod(grid[row:row+3])

      # col prod
      if col + 4 < num_cols:
        col_prod = prod(grid[col:col+4])

      # right diag
      if (row + 4 < num_rows) and (col + 4 < num_cols):
        pass

      # left diag
      if (row + 4 < num_rows) and (col - 4 > 0):
        pass

      pass

def createGrid(filename):
  grid = []
  f = open(filename, 'r')
  for line in f.readlines():
    num_list = map(int, line.strip().split())
    grid.append(num_list)

  return grid

def main():
  pp = pprint.PrettyPrinter(indent=1, width=100)

  grid = createGrid('small_grid.txt')
  pp.pprint(grid)

  findMaxProduct(grid)

if __name__ == "__main__":
      main()
