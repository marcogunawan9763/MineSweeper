"""
creates a 2D array representation of a minesweeper map, with 'b' representing mines
invoked using create_mine_map (n, m, num_bombs)
"""

import random
from typing import List, Any


def create_mine_map(n: int, m: int, num_bombs: int) -> List[List[Any]]:
  #create 2D array of mine_map
  mine_map = [[0 for i in range(m)] for j in range(n)]

  #place random mines into the map
  rand_mines = random.sample(range(n * m), num_bombs)
  mines = [int_to_matrix(mine, m) for mine in rand_mines]

  #name all the mines as b (for bomb)
  for mine in mines:
    mine_map[mine[0]][mine[1]] = 'b'

  #place the values of each tile based off how many mines are adjacent to it
  mine_map = value_map(n, m, mine_map)

  return mine_map

def int_to_matrix(value: int, m: int) -> tuple:
  return (value // m, value % m)

def value_map(n: int, m: int, mine_map: List[List[Any]]) -> List[List[Any]]:
  #orthogonal cardinatlity
  directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1)]

  #for each tile on the grid, if its not a bomb, count up how many bombs are around that tile
  for i in range(n):
    for j in range(m):
      if mine_map[i][j] == 'b':
        continue
      count = 0
      for dr in directions:
        new_row, new_col = i + dr[0], j+ dr[1]
        if new_row >= 0 and new_row < n and new_col >= 0 and new_col < m:
          if mine_map[new_row][new_col] == 'b':
            count += 1

      mine_map[i][j] = count

  return mine_map