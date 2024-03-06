def det(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("Input matrix must be a 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix_2=[[3,4],[1,2]]
result=det(matrix_2)
print("Determinant of 2*2 matrix",result)

