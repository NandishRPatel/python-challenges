from math import sqrt

class Sudoku(object):
	def __init__(self, data):
		self.data = data

	def is_valid(self):
		if len(self.data) > 0:
			if self.is_square():
				if self.is_valid_values():
					if self.is_valid_row_col_wise(self.data):
						boxes = [[i, i + int(sqrt(len(self.data)))] for i in range(0, len(self.data), int(sqrt(len(self.data))))]
						for n in range(len(boxes) - 1):
							if not self.is_little_square(boxes[n], set(self.data[0])): return False
						return True
					else: return False
				else: return False
			else: return False
		else: return False
		

	def is_square(self):
		return all(len(self.data) == len(row) for row in self.data)

	def is_valid_values(self):
		return all( (type(i) == type(1)) and ((i >= 1 and i <= len(self.data))) for row in self.data for i in row)

	def is_little_square(self, box, row):
		if set([self.data[i][j] for i in range(box[0], box[0] + int(sqrt(len(self.data)))) for j in range(box[1], box[1] + int(sqrt(len(self.data))))]) != row:
			return False
		return True


	def is_valid_row_col_wise(self, arr):
		arr_t = map(list, zip(*arr))
		return all(len(set(row)) == len(row) for row in arr) and all(len(set(row)) == len(row) for row in arr_t)

goodSudoku1 = Sudoku([
  [7,8,4, 1,5,9, 3,2,6],
  [5,3,9, 6,7,2, 8,4,1],
  [6,1,2, 4,3,8, 7,5,9],

  [9,2,8, 7,1,5, 4,6,3],
  [3,5,7, 8,4,6, 1,9,2],
  [4,6,1, 9,2,3, 5,8,7],
  
  [8,7,6, 3,9,4, 2,1,5],
  [2,4,3, 5,6,1, 9,7,8],
  [1,9,5, 2,8,7, 6,3,4]
])

goodSudoku2 = Sudoku([
  [1,4, 2,3],
  [3,2, 4,1],

  [4,1, 3,2],
  [2,3, 1,4]
])

# Invalid Sudoku
badSudoku1 = Sudoku([
  [0,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9],
  [1,2,3, 4,5,6, 7,8,9]
])

badSudoku2 = Sudoku([
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],  
  [1]
])

print(goodSudoku1.is_valid())
print(goodSudoku2.is_valid())
print(badSudoku1.is_valid())
print(badSudoku2.is_valid())