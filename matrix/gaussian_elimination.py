from fractions import Fraction

def row_div(mat,y,n):
	print("row %i /= %i" % (y,n))
	for x in range(len(mat[y])):
		mat[y][x] /= n
def row_submul(mat,base_row,diff_row,n):
	print("row %i -= %i * row %i" % (base_row,n,diff_row))
	for x in range(len(mat[base_row])):
		mat[base_row][x] -= mat[diff_row][x] * n
def first_nonzero(row):
	for i,e in enumerate(row):
		if e != 0:
			return i
	return -1
def upper(mat):
	width = len(mat[0])
	height = len(mat)
	for y in range(height):
		x = first_nonzero(mat[y])
		if x == -1:
			continue
		row_div(mat,y,mat[y][x])
		for yy in range(y + 1, height):
			row_submul(mat,yy,y,mat[yy][x])
	for y in reversed(range(height)):
		x = first_nonzero(mat[y])
		if x == -1:
			continue
		for yy in range(y):
			row_submul(mat,yy,y,mat[yy][x])
	return mat

def pr(matrix):
	def fp(e):
		if e.denominator == 1:
			return "%i" % e.numerator
		return "%i/%i" % (e.numerator,e.denominator)
	for row in matrix:
		print("".join(fp(e) + "\t" for e in row))
	print()

matrix = [
	[1,2,3,4],
	[5,6,7,-9],
	[9,-10,11,12]]
matrix = [[Fraction(e) for e in row] for row in matrix]

pr(upper(matrix))

#1x+2y+3z=4,5x+6y+7z=-9,9x-10y+11z=12