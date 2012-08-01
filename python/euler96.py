import numpy

def validNumber(number, puzzle):
	return True

def solveSudoku(puzzle):
	return puzzle[0][0]

puzzle = numpy.zeros(shape=(9,9))
print solveSudoku(puzzle)

puzzle[0][0] = 1
puzzle[1][2] = 4

print puzzle

def addLineToPuzzle(puzzle, line, lineNumber):
	linestuff = line.split()
	for x in range(0,9):
		puzzle[lineNumber%9][x] = linestuff[x]
	return puzzle

f = open('sudoku.txt')
lines = f.readlines()
lineNumber = 0
currentPuzzle = numpy.zeros(shape=(9,9))
for line in lines:
	foo = lineNumber % 10
	if (foo == 0):
		print currentPuzzle
		currentPuzzle = numpy.zeros(shape=(9,9))
		lineNumber = 0
	elif (foo % 10 > 0 and foo % 10 < 10):
		puzzle = addLineToPuzzle(currentPuzzle, line, lineNumber)
	lineNumber += 1



f.close()